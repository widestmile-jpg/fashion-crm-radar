"""Publish only a locally reviewed issue under issues/ via explicit GitHub approval."""
import os
from pathlib import Path

root = Path.cwd().resolve()
issue_folder = (root / "issues").resolve()
relative = os.environ.get("ISSUE_PATH", "")
candidate = (root / relative).resolve()

if not relative.startswith("issues/") or not relative.endswith(".html"):
    raise SystemExit("Only issues/*.html files are eligible for publication")
if issue_folder not in candidate.parents or not candidate.is_file():
    raise SystemExit("Issue must exist inside the issues directory")
html = candidate.read_text(encoding="utf-8")
if "<html" not in html.lower() or "<body" not in html.lower():
    raise SystemExit("Invalid HTML issue; refusing publication")
if len(html) < 1000:
    raise SystemExit("Issue appears incomplete; refusing publication")
(root / "index.html").write_text(html, encoding="utf-8")
print(f"Approved issue staged: {candidate.relative_to(root)}")
