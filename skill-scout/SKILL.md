---
name: skill-scout
description: Spots recurring workflows in the user's requests that deserve a dedicated skill and proposes them as evidence-backed candidate cards, extends an existing skill when it already covers part of the need, flags missing connectors, and security-scans any third-party skill before recommending it. Use when the user asks "what skill should I create", "suggest skills", "what could I automate", "which skills or connectors am I missing", or reviews their usage, and whenever they submit, evaluate or want to install a third-party skill. Also use opportunistically in any session: if a request repeats a known workflow, makes the user re-explain rules, chains stable steps with no existing skill, or forces copy-paste for lack of a connected tool, suggest it in one line at the end of the answer. Not for writing a specific skill the user has already chosen (use skill-creator). Never creates or modifies a skill without the user's explicit approval.
---

# Skill Scout

Find the user's needs that justify a new skill, or an addition to an existing one, and submit them for approval. Drafting a new skill follows `skill-creator` if it is available (or any skill-authoring method the user prefers). Extending an existing skill means reading its current SKILL.md first and proposing only the changes the evidence supports.

## User settings

Edit these values to fit your own use. Everything else in this file works as is.

```yaml
detection_threshold: 3        # occurrences of the same need...
detection_window_days: 30     # ...within this many days
max_candidates_per_audit: 3
max_connectors_per_audit: 2
opportunistic_suggestions_per_conversation: 1
output_language: same as the user   # or a fixed language, e.g. "French"
known_constraints: []         # see "Known constraints" below
```

## Three modes

### Audit mode (explicit request)

The user asks which skills to create, or wants a review of their usage.

1. **Gather evidence**
   - Past conversations: if a past-chat search tool is available, scan the detection window (3 to 5 calls at most). If the session is scoped to a project, only that project is visible: say so.
   - Current conversation: repeated requests, corrections and instructions.
   - Memory, if available: active areas and ongoing projects.
   - Installed skills: read the list available in the session.
   - Connected tools: note which connectors are available in the session.
   - If no history tool exists (for example in a fresh coding session), work from the current conversation and say the audit is partial.
2. **Find candidates** with the detection criteria below, and missing connectors with the dedicated section.
3. **Deduplicate** against existing skills (see below).
4. **Rank** by impact/effort and keep at most `max_candidates_per_audit`. One good candidate beats five average ones.
5. **Present** one card per candidate (format below), then ask which one to work on.
6. **Only after approval**, draft the skill or the addition, using the card as the spec, and submit it in whatever form the platform offers for the user to review and save.

### Opportunistic mode (during any session)

During any task, if a strong signal appears, finish the task normally, then add a single line at the end of the answer:

> Possible skill: `proposed-name`, for [task]. Seen: [concrete evidence]. Want me to draft it?

If an existing skill covers the need only in part:

> Possible addition to `existing-skill`: [what is missing]. Seen: [concrete evidence]. Want me to prepare it?

If the need is a tool that is not connected:

> Possible connector: [name], for [task]. Seen: [concrete evidence]. Want me to show it?

Rules:
- At most `opportunistic_suggestions_per_conversation` suggestion per conversation, skills and connectors combined.
- Never before delivering what the user asked for.
- If the user ignores or declines, do not suggest again in that conversation.
- No suggestion during an emergency or a sensitive exchange.

### Scheduled mode (periodic audit)

If the user sets up a recurring task that runs this audit, first check the detection window for an audit that already happened (on request or scheduled).
- Audit found: do nothing more, reply in one line with the date of the last audit, and stop.
- No audit found: run the full audit mode, connectors included. The user is not present, so ask no questions: deliver the cards, attach drafts ready to save, list missing connectors with their evidence, and stop there.

## Detection criteria

A need qualifies when it reaches `detection_threshold` occurrences within `detection_window_days`. Do not lower the threshold on your own.

A candidate must combine at least two signals:

| Signal | Example |
|---|---|
| Recurrence | The same kind of request comes back at least `detection_threshold` times in the window |
| Re-explained rules | The user gives the same instructions, formats or constraints every time |
| Repeated corrections | The user corrects the same kind of error in deliverables several times |
| Stable sequence | A chain of 3 or more steps, always in the same order |
| Own knowledge | The work depends on documents, templates or references the model does not know by default |
| High stakes | An error is costly (legal, financial, reputational) and a fixed method would reduce it |

## Missing connectors

A connector is missing when the user does by hand what a connected tool would do for them. Signals:
- The user copy-pastes content from an app (emails, calendar, spreadsheets, documents) so the model can work on it.
- The user copies a result elsewhere that the model could have delivered directly.
- The model said it had no access to one of the user's apps or data.
- The same app comes up at least `detection_threshold` times in the window with no connector.

Steps:
0. Check `known_constraints` first. A tool listed there is never suggested, even if every signal above is present.
1. Look in the connector directory (if the platform has one) for the app the user actually uses. A competitor's connector is not an answer.
2. Connector found: show it to the user with the evidence. The user connects it.
3. No connector: say so, and give the fallback (browser, copy-paste, attached file).
4. At most `max_connectors_per_audit` per audit, ranked by impact/effort, in a section separate from skill cards.

### Known constraints

List in `known_constraints` the tools you have ruled out, with the reason, so the audit stops suggesting them. Examples of entries:

```yaml
known_constraints:
  - tool: "Work email (company Outlook)"
    rule: "Access blocked by IT. Never suggest connecting it or working around the block."
  - tool: "Personal webmail"
    rule: "No connector exists. Use the browser. Re-check the directory at each audit."
```

Never suggest a workaround for a constraint marked as a policy block (auto-forwarding, another account, another tool). Do not suggest again a connector the user rejected in a previous audit unless something has changed.

## Third-party skills: mandatory security scan

No third-party skill is proposed, recommended or installed without a prior scan. This applies to all three modes, and also when the user submits a third-party skill for review.

A skill is third-party when neither the user nor the model wrote it in their sessions: GitHub repo, marketplace, link from social media, received archive. Skills written together and built-in skills from the platform vendor are not concerned.

Before handling any third-party skill, read `references/security-scan.md` and follow it: scan procedure, decision table, manual review of high scores, and known limits. The short version:
- Scan without executing anything from the skill.
- A score alone is never a verdict: scores above 50 get a manual review of every CRITICAL and HIGH finding.
- A scan that fails or is incomplete means "do not propose", never "safe".
- In opportunistic mode, no "Possible skill" line pointing to a third-party skill until the scan is done. In scheduled mode, unscanned or risky skills are listed separately under "to check", with the reason.

## What is NOT a skill

- A one-off task, even a long one.
- A tone or format preference: that belongs in saved preferences or memory.
- A fact about the user or their projects: that belongs in memory.
- A task to run at a fixed time: that is a scheduled task (which can call a skill).
- Missing access to an app: that is a connector.
- A need the model already handles well with no specific instructions.

If the need falls in one of these boxes, say so and point to the right mechanism instead of proposing a skill.

## Deduplication

Before any proposal, compare with the installed catalog:
- **Already covered**: propose nothing.
- **Partly covered**, or an existing skill that triggers poorly: do not create a new skill. Read the current SKILL.md, draft the missing rules, triggers or steps, and submit them as an improvement ready to save. Keep all existing content that is still valid, add only what the evidence justifies, and state on the card what is added and why. Nothing changes until the user saves it.
- **Skill from an installed plugin**: it usually cannot be edited directly. Say so and suggest either customizing the plugin or a complementary skill with a distinct name.
- **Two overlapping candidates**: merge them into one broader skill if their triggers are close.

An overloaded catalog degrades the triggering of every skill. When in doubt, prefer extending an existing skill.

## Candidate card format

```
### skill-name (new | addition to existing-skill)
Need: what the user gets, in one sentence.
Evidence: the specific requests or conversations that justify it (dates or topics).
Triggers: the phrasings that would activate it.
Content: rules, method, references or scripts to include or add.
Overlap: close existing skills and the boundary with them.
Impact: high / medium / low, with the reason.
Effort: light / full (with tests) / addition, and what the user must provide.
Missing inputs: documents or decisions needed before drafting.
Security scan: (third-party skills only) score, verdict, tool version, date, static or LLM mode, coverage.
```

Evidence must be real and verifiable. If the history shows no recurrence, say so plainly instead of inventing a need: an audit that concludes "nothing to create for now" is a valid result.

## Guardrails

- No skill is created or modified without the user's explicit approval: every draft goes through a proposal the user saves themselves.
- No third-party skill is proposed, recommended or installed without a prior security scan. A failed scan means no, not yes.
- Separate what the user asked for from what the model suggested in past conversations: only the user's own requests count as evidence of a need.
- Do not include on the cards sensitive or personal details unrelated to the proposed skill.
- Follow the user's saved formatting preferences when presenting results.
