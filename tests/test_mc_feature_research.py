"""Synthetic negative-path checks for a read-only research adapter, no game access."""
import copy
import importlib.util
import math
import struct
import sys
import unittest
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from mc_feature_research import compare_snapshots, decode_movement, exact, load_profile, masked_matches, native_type, capture, observe_mc_candidate


class FakeMemory:
    read_only = True
    base_address = 0x140000000

    def __init__(self, blocks=None):
        self.blocks = blocks or {}
        self.reads = []

    def is_alive(self):
        return True

    def read_bytes(self, address, size):
        self.reads.append((address, size))
        for start, raw in self.blocks.items():
            if start <= address and address + size <= start + len(raw):
                return raw[address - start:address - start + size]
        return None


class ReadOnlyResearchTests(unittest.TestCase):
    def setUp(self):
        self.profile = load_profile()

    def test_rw_handle_is_rejected_before_any_read(self):
        mem = FakeMemory()
        mem.read_only = False
        with self.assertRaisesRegex(PermissionError, 'READ_ONLY_HANDLE'):
            exact(mem, mem.base_address, 4)
        self.assertEqual(mem.reads, [])

    def test_short_read_is_not_silently_zero(self):
        mem = FakeMemory({0x10000: b'\0\0'})
        with self.assertRaisesRegex(OSError, 'UNREADABLE'):
            exact(mem, 0x10000, 4)

    def test_unknown_game_build_fails_before_section_scan(self):
        base = FakeMemory.base_address
        raw = bytearray(0x400)
        raw[:2] = b'MZ'
        struct.pack_into('<I', raw, 60, 0x80)
        raw[0x80:0x84] = b'PE\0\0'
        mem = FakeMemory({base: bytes(raw)})
        with self.assertRaisesRegex(ValueError, 'UNSUPPORTED_GAME_BUILD'):
            capture(mem, profile=self.profile)
        self.assertLessEqual(len(mem.reads), 2)

    def test_signature_mask_preserves_distinct_candidate_count(self):
        self.assertEqual(masked_matches(b'ABCxD--ABCyD', b'ABC_D', b'\xff\xff\xff\0\xff'), [0, 7])
        self.assertEqual(masked_matches(b'ABZxD', b'ABC_D', b'\xff\xff\xff\0\xff'), [])

    def test_side_mapping_and_nonfinite_value_rejection(self):
        raw = bytearray(2020)
        struct.pack_into('<I', raw, 0, 4)
        struct.pack_into('<2f', raw, 4 + 111 * 8, .4, .41)
        values = decode_movement(raw, self.profile)
        sides = values['tables']['current']['SpeedWithBallMinRating']
        self.assertEqual(sides['USER']['ui_scale_calculated'], 40)
        self.assertEqual(sides['CPU']['ui_scale_calculated'], 41)
        struct.pack_into('<f', raw, 4 + 111 * 8, math.nan)
        with self.assertRaisesRegex(ValueError, 'OUTSIDE_OBSERVED'):
            decode_movement(raw, self.profile)

    def test_native_field_drift_is_rejected(self):
        base = FakeMemory.base_address
        label = 'Value'
        crc = zlib.crc32(label.encode())
        profile = {'native_types': {'SYNTHETIC': {'rva': 0x100, 'field_count': 1, 'size': 8,
            'fields': {label: {'crc32': crc, 'offset': 0, 'size': 4, 'format': 0x23002000,
                              'array_words': [0, 0, 0], 'reference_rva': None}}}}}
        schema = bytearray(40)
        struct.pack_into('<I', schema, 20, 8)
        header = struct.pack('<8Q', 1, base + 0x300, 0, 0, base + 0x400, base + 0x500, 0, 0)
        bad_field = struct.pack('<10I', crc, 0, 4, 4, 0x23002000, 0, 0, 0, 0, 0)
        mem = FakeMemory({base + 0x100: header, base + 0x300: bad_field,
                          base + 0x400: bytes(schema), base + 0x500: b'SYNTHETIC\0'})
        with self.assertRaisesRegex(ValueError, 'LAYOUT_MISMATCH'):
            native_type(mem, profile, 'SYNTHETIC')

    def test_compare_distinguishes_restoration_from_retained_custom_cache(self):
        before = {'process': {'pid': 1, 'creation_time': 'synthetic'}, 'native': {'synthetic': True},
                  'movement': {'object_address_local_only': 0x10000, 'raw_saved_local_only': bytes(2020).hex()}}
        after = copy.deepcopy(before)
        raw = bytearray(2020)
        struct.pack_into('<f', raw, 0x3f4, .4)
        after['movement']['raw_saved_local_only'] = raw.hex()
        result = compare_snapshots(before, after)
        self.assertTrue(result['preset_restored'])
        self.assertTrue(result['current_table_restored'])
        self.assertFalse(result['custom_cache_identical'])
        after['process']['creation_time'] = 'different-process'
        with self.assertRaisesRegex(ValueError, 'DIFFERENT_PROCESS'):
            compare_snapshots(before, after)

    def test_cli_refuses_output_outside_exports(self):
        spec = importlib.util.spec_from_file_location('dev09_cli', ROOT / 'scripts/research_mc_features.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with self.assertRaisesRegex(ValueError, 'EXPORTS_JSON'):
            module.output_path(ROOT / 'published/DEV09_FORBIDDEN.json')

    def test_mc_candidate_requires_name_before_reading(self):
        mem = FakeMemory()
        with self.assertRaisesRegex(ValueError, 'MC_NAME_REQUIRED'):
            observe_mc_candidate(mem, self.profile, '')
        self.assertEqual(mem.reads, [])


if __name__ == '__main__':
    unittest.main()
