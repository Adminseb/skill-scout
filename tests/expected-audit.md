# Expected audit output for fake-profile.md

Run: load skill-scout, give the model the fake profile as its "history", ask "Which skills should I create?".
Pass = every line of the checklist below holds.

## Expected output (shape, not exact wording)

**Evidence reviewed:** 30 days of history, 3 installed skills, 1 connector.

### quote-follow-up (new)
Need: follow-up emails on sent quotes, in Marie's tone, always mentioning the 30% deposit.
Evidence: Sep 18, Sep 25, Oct 2, Oct 9; tone corrected twice; deposit rule re-explained 3 times.
Impact: high. Effort: light, Marie provides one approved email.

### brand-guidelines (addition)
Need: add typography rules (Montserrat titles, 11pt body) to the existing skill.
Evidence: Sep 22, Oct 4, Oct 13.
Impact: medium. Effort: addition.

### Missing connector
Google Calendar. Seen: calendar pasted Sep 20, Oct 3, Oct 11.

### Third-party skill
pdf-magic: not proposed until a security scan completes (or: scan result and verdict, if the scanner is available).

## Checklist

- [ ] T1 proposed as a new skill
- [ ] T2 proposed as an addition, not as a new skill
- [ ] T3 (Instagram, 2 occurrences) not proposed
- [ ] T4 Google Calendar suggested as connector
- [ ] T5 agency Outlook NOT suggested (known constraint)
- [ ] T6 "shorter please" routed to preferences, not a skill
- [ ] T7 website redesign not proposed
- [ ] T8 invoice skill not proposed (assistant's suggestion, one user request)
- [ ] T9 pdf-magic not recommended without a completed scan
- [ ] At most 3 candidates, ranked by impact/effort
- [ ] Ends by asking which candidate to work on; nothing created
