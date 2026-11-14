# Example: audit mode

> **User:** Which skills should I create?

**Evidence reviewed:** 30 days of conversations (4 searches), memory, 18 installed skills, 5 connectors.

### invoice-reminder-emails (new)
Need: draft polite payment reminders in the company's tone, escalating by delay.
Evidence: 4 requests between Sept 2 and Sept 27; tone corrected twice ("too aggressive", "add the invoice number").
Triggers: "write a payment reminder", "chase this invoice".
Content: three reminder levels (7, 15, 30 days), mandatory fields, tone rules.
Overlap: none.
Impact: high, recurring and visible to clients.
Effort: light. You provide one reminder you were happy with.
Missing inputs: legal mention for late fees, if any.

### meeting-minutes (addition to existing `meeting-notes`)
Need: the existing skill misses the action-items table you add by hand each time.
Evidence: table added manually on Sept 5, 12 and 19.
Triggers: unchanged.
Content: add an "Actions / Owner / Deadline" table at the end.
Overlap: this is the skill itself.
Impact: medium.
Effort: addition.
Missing inputs: none.

### Missing connector
**Google Calendar**, for scheduling follow-ups. Seen: you pasted your agenda on Sept 8, 15 and 22.

Which one should I work on first?

---

# Example: opportunistic mode

> *(end of an unrelated answer)*
>
> Possible skill: `supplier-quote-comparison`, for comparing supplier quotes. Seen: third time this month you've asked for the same comparison table. Want me to draft it?

---

# Example: third-party skill review

> **User:** Should I install this skill I found on GitHub?

Security scan (SkillSpector, static mode): score 62, DO_NOT_INSTALL.
Manual review of 2 HIGH findings: both false positives (the word "sudo" in a code example in the docs; a call to the vendor's own official API). Treated as CAUTION.
MEDIUM findings were not reviewed one by one.
I also read the SKILL.md and the one script: nothing unexpected. A clean read lowers the risk but does not prove the skill is harmless. Your call.
