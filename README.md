# skill-scout

A Claude skill that watches how you work and tells you which skills you should actually build.

Most people end up re-typing the same instructions, the same formats and the same rules every week. skill-scout notices that. It looks for needs that keep coming back, checks them against the skills you already have, and proposes a short, evidence-backed card for each real candidate. It never creates anything without your approval.

It also does two things most skill collections don't:

- **Flags missing connectors.** If you keep copy-pasting from the same app, it tells you a connector would do the job.
- **Scans third-party skills before recommending them.** Any skill you didn't write goes through a static security scan ([SkillSpector](https://github.com/NVIDIA/skillspector)) with clear decision rules, including a manual review step to sort real risks from false positives.

## How it works

| Mode | When | What it does |
|---|---|---|
| Audit | You ask "what skills should I create?" | Reviews recent conversations, memory, installed skills and connectors, then proposes up to 3 ranked candidates |
| Opportunistic | During any session | When a strong signal shows up, adds one line at the end of the answer. Once per conversation, never during urgent work |
| Scheduled | A recurring task you set up | Runs the audit unattended, skips if one already ran in the window |

A need qualifies when it shows up at least 3 times in 30 days **and** combines two signals: recurrence, re-explained rules, repeated corrections, stable multi-step sequence, knowledge the model lacks, or high stakes. If nothing qualifies, it says so. "Nothing to create for now" is a valid result.

## Example output

```
### weekly-client-report (new)
Need: turn raw sales exports into the client report format in one step.
Evidence: same request on Oct 3, Oct 10, Oct 17 and Oct 24; format re-explained 3 times.
Triggers: "make the weekly report", "client report from this export".
Content: report template, column mapping, rounding rules, tone guidelines.
Overlap: none; the xlsx skill handles files, not this format.
Impact: high, saves ~20 min per week and removes recurring formatting errors.
Effort: light. You provide one approved past report.
Missing inputs: final template.
```

More in [`examples/`](examples/).

## Install

**Claude.ai / Claude desktop:** zip the `skill-scout/` folder and upload it in Settings > Capabilities > Skills.

**Claude Code:** copy the `skill-scout/` folder into `~/.claude/skills/` (personal) or `.claude/skills/` (project).

Then ask: *"Which skills should I create?"*

## What's in the folder

- `skill-scout/SKILL.md`: the skill itself.
- `skill-scout/references/security-scan.md`: the third-party scan procedure, loaded only when needed.

## Configure

Open `skill-scout/SKILL.md` and edit the **User settings** block: detection threshold, window, number of candidates, output language, and a list of tools you've ruled out (for example a work mailbox blocked by IT) so it stops suggesting them.

## Works best with

- Past-chat search and memory turned on (the audit is richer with history).
- `skill-creator` installed, to draft and test approved candidates.
- Python 3.12+ and `uv`, for the security scan.

Without history tools, skill-scout still works from the current conversation and tells you the audit is partial.

## Limits

- It can only see what the platform lets it see. A project-scoped chat only sees that project.
- The security scan is static: it lowers the risk, it does not prove a skill is safe. skill-scout says so every time.
- It proposes; you decide. Nothing is saved without you.

## Testing

`tests/fake-profile.md` is a fake 30-day history with nine traps (real candidates, near misses, a blocked tool, a third-party skill). `tests/expected-audit.md` lists what a correct audit must and must not propose. If you change the detection rules, replay it.

`python3 tests/validate.py` checks the skill's structure (frontmatter, description length, referenced files).

## Contributing

Issues and pull requests are welcome, especially:
- false positives or missed signals you've seen in real audits,
- better detection criteria,
- support for other security scanners.

Please keep examples free of personal data.

## License

MIT, see [LICENSE](LICENSE).
