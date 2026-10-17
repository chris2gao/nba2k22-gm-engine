# NBA2K22 GM project instructions

- Read docs/22_DATA_SOURCE_AND_DECISION_GOVERNANCE.md for truth/approval rules; docs/24_DATA_SOURCE_REGISTRY_AND_PLAYER_TRIGGERS.md for data jobs; docs/25_GITHUB_AND_WEB_GM_PROTOCOL.md for web handoff. Avoid loading every historical design document for a data update.
- The player alone triggers data updates and supplies the game date and career ID. Game dates are player-confirmed context, not currently observed memory fields. No calendar scheduling or autonomous gameplay progression.
- Use scripts/run_data_update.ps1 for a player-triggered update. The scripts perform calibration, capture, audit, computation, export and optional private publication without a model. Use a separate terminal with -NewWindow when requested.
- Historical SQLite snapshots remain facts at their capture time; process pointers are runtime-only. Recalibrate each collection, fail closed on unreadable/invalid data, and never invent missing game statistics.
- Any numeric reasoning must use Python/SQL or an existing deterministic result. A schema column does not establish that its value is observed.
- Actual game writes, execution of trades, and changes to formal team decision documents or decision execution scripts require player approval of the concrete proposal. Read-only capture, audits, data exporter maintenance and a requested private data sync are separate from game decision execution.
- Never stage live database files, runtime maps, local logs, backups or credentials. Audited derived JSON is versioned under published/; SQLite archives are private Release assets. Preserve exact published file bytes.
- The data-only publisher must not commit unrelated staged changes, force push or publish a source-code revision it did not review. No credential files or secrets may be read or committed.
- Web decisions cite career, batch and commit. Worldline fiction and real NBA references never overwrite observed game facts. Remote decision intake/execution is not implemented; never treat a remote approved=true field as human approval.
