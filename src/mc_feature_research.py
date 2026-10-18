"""DEV09 read-only native-schema and movement-setting research.

This module has no writer, injection, UI control, or automatic mode detector.
Caller-supplied mode/menu labels are context, never automatic observations.
"""
import json
import math
import struct
import zlib
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


def load_profile(path=None):
    path = path or Path(__file__).resolve().parents[1] / 'config/mc_features_research_profile.json'
    return json.loads(Path(path).read_text(encoding='utf-8'))


def exact(mem, address, size):
    if getattr(mem, 'read_only', None) is not True:
        raise PermissionError('RESEARCH_REQUIRES_READ_ONLY_HANDLE')
    if not isinstance(address, int) or not 0x10000 <= address < 0x800000000000:
        raise ValueError('INVALID_RESEARCH_ADDRESS')
    if not isinstance(size, int) or not 0 < size <= 64 * 1024 * 1024:
        raise ValueError('RESEARCH_READ_BOUND')
    raw = mem.read_bytes(address, size)
    if raw is None or len(raw) != size:
        raise OSError('RESEARCH_MEMORY_UNREADABLE')
    return raw


def masked_matches(raw, pattern, mask):
    if not pattern or len(pattern) != len(mask) or mask[0] != 255:
        raise ValueError('INVALID_RESEARCH_SIGNATURE')
    anchor_end = next((i for i, value in enumerate(mask) if value != 255), len(mask))
    anchor = pattern[:anchor_end]
    result, pos = [], 0
    while True:
        pos = raw.find(anchor, pos)
        if pos < 0:
            return result
        candidate = raw[pos:pos + len(pattern)]
        if len(candidate) == len(pattern) and all((a & m) == (b & m) for a, b, m in zip(candidate, pattern, mask)):
            result.append(pos)
        pos += 1


def native_type(mem, profile, name):
    spec = profile['native_types'][name]
    header = struct.unpack('<8Q', exact(mem, mem.base_address + spec['rva'], 64))
    if header[0] != spec['field_count'] or not 0 < header[0] < 2000:
        raise ValueError('NATIVE_FIELD_COUNT_MISMATCH_' + name)
    if exact(mem, header[5], len(name) + 1) != name.encode() + b'\0':
        raise ValueError('NATIVE_TYPE_NAME_MISMATCH_' + name)
    schema = struct.unpack('<10I', exact(mem, header[4], 40))
    if schema[5] != spec['size']:
        raise ValueError('NATIVE_TYPE_SIZE_MISMATCH_' + name)
    table = exact(mem, header[1], header[0] * 40)
    fields = {}
    for i in range(header[0]):
        row = struct.unpack_from('<10I', table, i * 40)
        if row[0] in fields:
            raise ValueError('DUPLICATE_NATIVE_FIELD')
        fields[row[0]] = row
    for label, expected in spec['fields'].items():
        crc = zlib.crc32(label.encode())
        if crc != expected['crc32'] or crc not in fields:
            raise ValueError('NATIVE_FIELD_MISSING_' + label)
        row = fields[crc]
        reference = row[8] | row[9] << 32
        wanted_reference = mem.base_address + expected['reference_rva'] if expected['reference_rva'] is not None else 0
        if (row[2:5] != (expected['offset'], expected['size'], expected['format'])
                or list(row[5:8]) != expected['array_words'] or reference != wanted_reference):
            raise ValueError('NATIVE_FIELD_LAYOUT_MISMATCH_' + label)
    return {'status': 'CURRENT_PROCESS_SCHEMA_VERIFIED', 'size': spec['size'], 'verified_fields': list(spec['fields'])}


def verify_takeover_enum(mem, profile):
    spec = profile['takeover_enum']
    header = struct.unpack('<6Q', exact(mem, mem.base_address + spec['rva'], 48))
    if header[2] != len(spec['values']):
        raise ValueError('TAKEOVER_ENUM_COUNT_MISMATCH')
    raw = exact(mem, header[3], header[2] * 12)
    actual = {}
    for i in range(header[2]):
        crc, value, _ = struct.unpack_from('<IiI', raw, i * 12)
        label = spec['values'].get(str(value))
        if value in actual or label is None or crc != zlib.crc32(label.encode()):
            raise ValueError('TAKEOVER_ENUM_MISMATCH')
        actual[value] = label
    return actual


def decode_movement(raw, profile):
    if len(raw) != 2020:
        raise ValueError('INVALID_TUNEDATA_SAVED_SIZE')
    result = {'game_style_raw': struct.unpack_from('<I', raw)[0], 'tables': {}}
    for table, table_offset in [('current', 4), ('custom', 0x3f4)]:
        fields = {}
        for name, field in profile['movement']['fields'].items():
            fields[name] = {}
            for side, column in profile['movement']['sides'].items():
                offset = table_offset + field['table_index'] * 8 + column * 4
                value = struct.unpack_from('<f', raw, offset)[0]
                if not math.isfinite(value) or not 0 <= value <= 1:
                    raise ValueError('MOVEMENT_VALUE_OUTSIDE_OBSERVED_NATIVE_SCALE')
                fields[name][side] = {'raw_float': value, 'raw_hex': raw[offset:offset + 4].hex(),
                                      'object_offset': offset, 'ui_scale_calculated': round(value * 100, 4)}
        result['tables'][table] = fields
    return result


def capture(mem, mode_context='UNKNOWN', ui_side_context='UNKNOWN', profile=None):
    profile = profile or load_profile()
    if mode_context not in ('UNKNOWN', 'PLAYER_CONFIRMED_MYLEAGUE_TEST', 'PLAYER_CONFIRMED_MC'):
        raise ValueError('INVALID_PLAYER_MODE_CONTEXT')
    if ui_side_context not in ('UNKNOWN', 'CPU', 'USER'):
        raise ValueError('INVALID_PLAYER_SIDE_CONTEXT')
    if not getattr(mem, 'is_alive', lambda: False)():
        raise RuntimeError('RESEARCH_PROCESS_NOT_LIVE')
    base = mem.base_address
    dos = exact(mem, base, 64)
    peoff = struct.unpack_from('<I', dos, 60)[0]
    if dos[:2] != b'MZ' or not 64 <= peoff <= 4096:
        raise ValueError('INVALID_GAME_PE_HEADER')
    pe = exact(mem, base + peoff, 0x108)
    expected = profile['expected_pe']
    if (pe[:4] != b'PE\0\0' or struct.unpack_from('<H', pe, 4)[0] != expected['machine']
            or struct.unpack_from('<H', pe, 24)[0] != 0x20b
            or struct.unpack_from('<I', pe, 8)[0] != expected['timestamp']
            or struct.unpack_from('<I', pe, 0x50)[0] != expected['image_size']):
        raise ValueError('UNSUPPORTED_GAME_BUILD_RESEARCH_ONLY')
    count, optional = struct.unpack_from('<H', pe, 6)[0], struct.unpack_from('<H', pe, 20)[0]
    if not 0 < count <= 40 or not 0x70 <= optional <= 0x1000:
        raise ValueError('INVALID_GAME_SECTION_TABLE')
    section_raw = exact(mem, base + peoff + 24 + optional, count * 40)
    sections = []
    for i in range(count):
        pos = i * 40
        name = section_raw[pos:pos + 8].rstrip(b'\0')
        size, rva = struct.unpack_from('<II', section_raw, pos + 8)
        if rva + size > expected['image_size']:
            raise ValueError('GAME_SECTION_OUT_OF_BOUNDS')
        sections.append((name, rva, size))
    code_sections = [s for s in sections if s[0] == b'.text']
    if len(code_sections) != 1:
        raise ValueError('AMBIGUOUS_GAME_CODE_SECTION')
    _, code_rva, code_size = code_sections[0]
    code = exact(mem, base + code_rva, code_size)
    movement = profile['movement']
    pattern, mask = bytes.fromhex(movement['getter_bytes']), bytes.fromhex(movement['getter_mask'])
    hits = masked_matches(code, pattern, mask)
    if len(hits) != 1:
        raise ValueError('MOVEMENT_GETTER_NOT_UNIQUE')
    getter = base + code_rva + hits[0]
    getter_raw = code[hits[0]:hits[0] + len(pattern)]
    targets = []
    for key in ('pointer_instruction_offset', 'mapping_instruction_offset'):
        pos = movement[key]
        target = getter + pos + 7 + struct.unpack_from('<i', getter_raw, pos + 3)[0]
        if not any(name == b'.data' and base + rva <= target < base + rva + size for name, rva, size in sections):
            raise ValueError('NATIVE_GETTER_TARGET_OUTSIDE_DATA')
        targets.append(target)
    pointer_slot, mapping = targets
    if pointer_slot % 8:
        raise ValueError('UNALIGNED_SETTINGS_POINTER')
    for field in movement['fields'].values():
        index = struct.unpack('<i', exact(mem, mapping + field['native_id'] * 4, 4))[0]
        if index != field['table_index'] or not 0 <= index < movement['table_count']:
            raise ValueError('NATIVE_MOVEMENT_INDEX_MISMATCH')
        crc = struct.unpack('<I', exact(mem, base + movement['name_crc_array_rva'] + field['native_id'] * 4, 4))[0]
        if crc != field['crc32']:
            raise ValueError('NATIVE_MOVEMENT_NAME_CRC_MISMATCH')
    schemas = {name: native_type(mem, profile, name) for name in profile['native_types']}
    takeover_enum = verify_takeover_enum(mem, profile)
    obj = struct.unpack('<Q', exact(mem, pointer_slot, 8))[0]
    raw = exact(mem, obj, 2020)
    values = decode_movement(raw, profile)
    if (exact(mem, pointer_slot, 8) != struct.pack('<Q', obj) or exact(mem, obj, 2020) != raw
            or not mem.is_alive()):
        raise RuntimeError('SOURCE_CHANGED_DURING_RESEARCH_CAPTURE')
    return {'task': profile['task'], 'status': 'READ_ONLY_RESEARCH_SNAPSHOT',
            'observed_at': datetime.now(timezone.utc).isoformat(),
            'process': {'pid': mem.pid, 'creation_time': mem.creation_time, 'module_base_local_only': base},
            'player_supplied_context': {'mode': mode_context, 'ui_side': ui_side_context,
                                        'automatically_detected': False},
            'native': {'pe': expected, 'getter_rva': getter - base, 'pointer_slot_rva': pointer_slot - base,
                       'index_map_rva': mapping - base, 'name_crc_array_rva': movement['name_crc_array_rva'],
                       'schemas': schemas},
            'movement': {'object_address_local_only': obj, 'raw_saved_local_only': raw.hex(), **values,
                         'gameplay_consumer': 'UNVERIFIED', 'mc_effective_instance': 'UNVERIFIED'},
            'mc': {'current_player_identity': 'NOT_BOUND', 'values_observed': False,
                   'takeover_enum': takeover_enum, 'gatorade_state': 'SCHEMA_ONLY',
                   'weekly_workout_state': 'UNRESOLVED', 'gym_rat_effect': 'UNVERIFIED'},
            'game_writes': 0, 'execution_authorized': False, 'production_source': False}


def compare_snapshots(before, after):
    if before['process'] != after['process']:
        raise ValueError('DIFFERENT_PROCESS_OR_MODULE')
    left, right = before['movement'], after['movement']
    if left['object_address_local_only'] != right['object_address_local_only'] or before['native'] != after['native']:
        raise ValueError('DIFFERENT_NATIVE_SETTINGS_BINDING')
    a, b = bytes.fromhex(left['raw_saved_local_only']), bytes.fromhex(right['raw_saved_local_only'])
    if len(a) != 2020 or len(b) != 2020:
        raise ValueError('INVALID_COMPARISON_SNAPSHOT')
    changes = [{'object_offset': i, 'before_hex': a[i:i + 4].hex(), 'after_hex': b[i:i + 4].hex()}
               for i in range(0, len(a), 4) if a[i:i + 4] != b[i:i + 4]]
    return {'status': 'SAME_PROCESS_SETTINGS_DIFFERENTIAL', 'changes': changes,
            'current_table_restored': a[4:0x3f4] == b[4:0x3f4], 'preset_restored': a[:4] == b[:4],
            'custom_cache_identical': a[0x3f4:] == b[0x3f4:], 'game_writes': 0}


def observe_mc_candidate(mem, profile, expected_name):
    """Read a CAREERMODE-indexed player only after explicit MC/name context.

    This binds a local data candidate. UI type/effect and live gameplay identity
    still require independent confirmation; no name-only roster search fallback.
    """
    if not isinstance(expected_name, str) or not expected_name.strip():
        raise ValueError('PLAYER_CONFIRMED_MC_NAME_REQUIRED')
    bindings = profile['mc_binding_candidates']
    base = mem.base_address
    rva = bindings['career_reference_instruction_rva']
    expected = bytes.fromhex(bindings['career_instruction_bytes'])
    code = exact(mem, base + rva, len(expected))
    if code != expected:
        raise ValueError('CAREER_NATIVE_REFERENCE_MISMATCH')
    career_slot = base + rva + 7 + struct.unpack_from('<i', code, 3)[0]
    career = struct.unpack('<Q', exact(mem, career_slot, 8))[0]
    player_index = struct.unpack('<H', exact(mem, career, 2))[0]
    roster_rva = bindings['roster_getter_rva']
    getter = exact(mem, base + roster_rva, 8)
    wanted = bytes.fromhex(bindings['roster_getter_bytes'])
    if getter != wanted or getter[7:] != b'\xc3':
        raise ValueError('MC_ROSTER_NATIVE_GETTER_MISMATCH')
    roster_slot = base + roster_rva + 7 + struct.unpack_from('<i', getter, 3)[0]
    roster = struct.unpack('<Q', exact(mem, roster_slot, 8))[0]
    root = roster - 8
    count = struct.unpack('<Q', exact(mem, root + 0x18, 8))[0]
    players = struct.unpack('<Q', exact(mem, root + 0x20, 8))[0]
    end = struct.unpack('<Q', exact(mem, root + 0x30, 8))[0]
    if not 0 < count <= 100000 or end != players + count * 0x4f0 or players != root + 0x4f0:
        raise ValueError('MC_ROSTER_DIRECTORY_INVALID')
    if player_index >= count:
        raise ValueError('MC_PLAYER_INDEX_OUTSIDE_ROSTER')
    address = players + player_index * 0x4f0
    player = exact(mem, address, 0x4f0)
    last = player[:40].decode('utf-16le', errors='strict').split('\0')[0]
    first = player[0x28:0x50].decode('utf-16le', errors='strict').split('\0')[0]
    full_name = (first + ' ' + last).strip()
    normalize = lambda value: ' '.join(unicodedata.normalize('NFKC', value).casefold().split())
    if normalize(full_name) != normalize(expected_name):
        raise ValueError('CAREER_INDEX_NAME_MISMATCH_ACTUAL_' + full_name)
    blacktop = struct.unpack_from('<Q', player, 0xe0)[0]
    raw = exact(mem, blacktop, 0xd4)
    fields = profile['native_types']['BLACKTOPDATA']['fields']
    observed = {}
    for label, field in fields.items():
        off, size, fmt = field['offset'], field['size'], field['format']
        word = int.from_bytes(raw[off:off + size], 'little')
        start, width = (fmt >> 16) & 255, (fmt >> 8) & 255
        value = (word >> start) & ((1 << width) - 1)
        observed[label] = {'raw': value, 'whole_storage_hex': raw[off:off + size].hex(),
                           'semantics': 'NATIVE_FIELD_ONLY_EFFECT_UNVERIFIED'}
    gym = profile['native_types']['PLAYERDATA']['fields']['CareerGymEliminatorBadge']
    gym_word = player[gym['offset']]
    observed['CareerGymEliminatorBadge'] = {'raw': (gym_word >> 1) & 1,
        'whole_storage_hex': bytes([gym_word]).hex(), 'semantics': 'GYM_RAT_CANDIDATE_BADGE_WRITES_FORBIDDEN'}
    if (exact(mem, career_slot, 8) != struct.pack('<Q', career)
            or exact(mem, roster_slot, 8) != struct.pack('<Q', roster)
            or exact(mem, career, 2) != struct.pack('<H', player_index)
            or exact(mem, player_index * 0x4f0 + players, 0x4f0) != player
            or exact(mem, blacktop, 0xd4) != raw or not mem.is_alive()):
        raise RuntimeError('MC_SOURCE_CHANGED_DURING_READ')
    return {'status': 'CAREER_INDEX_ROSTER_NAME_MATCHED_LOCAL_CANDIDATE',
            'display_name': full_name, 'native_unique_id': struct.unpack_from('<H', player, 0xf4)[0],
            'roster_index_local_only': player_index, 'player_address_local_only': address,
            'blacktop_address_local_only': blacktop, 'fields': observed,
            'takeover_label': profile['takeover_enum']['values'].get(str(observed['CareerModeTakeoverArchetype']['raw'])),
            'ui_type_confirmation': 'PENDING', 'live_gameplay_effect': 'UNVERIFIED', 'game_writes': 0}
