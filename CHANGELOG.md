# Changelog

## 1.0.0 (2026-11-15)

First public release.

- Three modes: audit, opportunistic, scheduled.
- Detection criteria with a configurable threshold (default: 3 occurrences in 30 days, two signals).
- Missing-connector detection, with user-defined known constraints.
- Mandatory security scan for third-party skills (SkillSpector), in `references/security-scan.md`.
- Test fixture: fake 30-day profile with nine traps and the expected audit.
