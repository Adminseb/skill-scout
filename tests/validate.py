"""Structural checks for the skill. Run: python3 tests/validate.py"""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
skill = root / "skill-scout" / "SKILL.md"
text = skill.read_text(encoding="utf-8")
errors = []

m = re.match(r"---\n(.*?)\n---\n", text, re.S)
if not m:
    errors.append("missing frontmatter")
else:
    fm = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l)
    if fm.get("name") != "skill-scout":
        errors.append("name must be 'skill-scout'")
    d = fm.get("description", "")
    if not 50 <= len(d) <= 1024:
        errors.append(f"description length {len(d)} not in 50..1024")
    if "<" in d or ">" in d:
        errors.append("description contains angle brackets")

if len(text.splitlines()) > 500:
    errors.append("SKILL.md over 500 lines")

for ref in re.findall(r"`(references/[^`]+)`", text):
    if not (skill.parent / ref).exists():
        errors.append(f"missing referenced file: {ref}")

for needed in ["README.md", "LICENSE", "CHANGELOG.md", "tests/fake-profile.md", "tests/expected-audit.md"]:
    if not (root / needed).exists():
        errors.append(f"missing {needed}")

if errors:
    print("FAIL"); [print(" -", e) for e in errors]; sys.exit(1)
print("OK")
