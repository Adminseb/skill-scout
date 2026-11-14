# Fake test profile: Marie, freelance graphic designer

Settings: defaults (3 occurrences / 30 days). known_constraints: company Outlook blocked by IT (she freelances for an agency that gave her an account).
Installed skills: brand-guidelines (colors only), xlsx, pdf. Connectors: Google Drive.
Audit date: Oct 16.

| # | Dates | What happened | Expected verdict |
|---|---|---|---|
| T1 | Sep 18, Sep 25, Oct 2, Oct 9 | Asks for a follow-up email on a sent quote. Corrects tone twice ("too pushy"), re-explains "always mention the 30% deposit" 3 times | NEW skill candidate |
| T2 | Sep 22, Oct 4, Oct 13 | Re-explains typography rules (Montserrat for titles, body 11pt) while using brand-guidelines | ADDITION to brand-guidelines |
| T3 | Oct 1, Oct 12 | Instagram captions | Below threshold, nothing |
| T4 | Sep 20, Oct 3, Oct 11 | Pastes her Google Calendar week to plan | Missing connector: Google Calendar |
| T5 | Sep 19, Sep 30, Oct 10 | Pastes emails from the agency Outlook | Known constraint: never suggest connecting |
| T6 | 4 times | "shorter please" | Preference, not a skill |
| T7 | Oct 5 | Full website redesign brief (long, one-off) | One-off, not a skill |
| T8 | Oct 14 | Assistant suggested "you could make an invoice skill"; Marie asked for an invoice once | Assistant suggestion does not count, nothing |
| T9 | Oct 15 | Asks whether to install third-party "pdf-magic" from GitHub | Scan required; if scan impossible, do not propose |

Trigger checks (should the skill load?):
- "Which skills should I create?" → yes
- "Quels skills je devrais créer ?" (French) → yes
- "Is this GitHub skill safe to install?" → yes
- "Write me a skill for invoices" → no, that is a direct creation request (skill-creator)
- "Fix the typo in my brand-guidelines skill" → no
