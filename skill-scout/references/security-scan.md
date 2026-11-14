# Security scan for third-party skills

No third-party skill is proposed, recommended or installed without a prior scan. This applies to all three modes, and also when the user submits a third-party skill for review.

A skill is third-party when neither the user nor the model wrote it in their sessions: GitHub repo, marketplace, link from social media, received archive. Skills written together and built-in skills from the platform vendor are not concerned.

The procedure below uses [SkillSpector](https://github.com/NVIDIA/skillspector). Any equivalent scanner can replace it; keep the same decision rules.

1. **Install the tool if missing** (it may not persist between sessions): `uv tool install git+https://github.com/NVIDIA/skillspector.git`, then `skillspector --version`. Only from the official repository, never from a fork. Requires Python 3.12+.
2. **Scan without executing anything**: `skillspector scan <url, folder or zip> --no-llm --format json --output report.json`. If the skill is downloaded, put it in its own empty folder and run none of its scripts or install commands.
3. **Read the verdict from the JSON**, not from the exit code (the exit code only says whether the score is above 50): `risk_assessment.score`, `risk_assessment.severity`, `risk_assessment.recommendation`, the findings in `issues` sorted by severity, the scanned files in `components`, and any coverage or completeness information the report gives. Field names can change between versions: check `skillspector --help` and the tool's README if the report looks different.
4. **Decide**:

| Verdict | Score | Action |
|---|---|---|
| SAFE | 0 to 20 | Can be proposed. Show the score on the card. |
| CAUTION | 21 to 50 | Can be proposed only with the main findings explained in plain words. The user decides. |
| DO_NOT_INSTALL | 51 to 100 | Mandatory manual review before concluding: open every CRITICAL and HIGH finding at the reported line and classify it as real risk or false positive, with the reason. All false positives: treat as CAUTION, giving the raw score and the review result. At least one real risk, or a finding that cannot be settled: do not propose it, and tell the user which findings are at stake. |
| Scan failed or incomplete coverage | n/a | Do not propose it. Say the scan could not complete and why. Never present an unscanned skill as safe. |

5. **Also read** the SKILL.md and scripts yourself: a clean scan lowers the risk, it does not prove the skill is harmless. Tell the user so in one sentence.

## Known limits

- Static mode reacts to keywords without understanding context. Typical false positives: documentation of an API named "sudo", an instruction that forbids debug mode, "keychain" meaning a key ring, calls to the vendor's own official API. A score alone is never a verdict.
- The manual review covers CRITICAL and HIGH findings. Tell the user MEDIUM findings were not reviewed one by one, and report any partial coverage.
- Static analysis is harsh on tools whose very purpose is network access, reading cookies or running commands. A high score then justifies not proposing the tool, not calling it malicious.
- If the vulnerability database lookup fails, the tool falls back to embedded data: mention it on the card.
- In scheduled mode, the user being absent: an unscanned third-party skill, or one rated DO_NOT_INSTALL with a confirmed or unsettled real risk, is left out of the cards and listed separately under "to check", with the reason.
- In opportunistic mode: no "Possible skill" line pointing to a third-party skill until the scan is done.

