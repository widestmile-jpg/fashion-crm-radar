"""Smoke test only: render an existing anonymized reconstruction, not a Gmail original."""
from pathlib import Path
from playwright.sync_api import sync_playwright

SOURCE = Path("sources/1a16395a51e65ad5.html").resolve()
OUT = Path("screenshot-test")
OUT.mkdir(exist_ok=True)
assert SOURCE.is_file(), "The anonymized reference HTML is missing"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 760, "height": 900}, device_scale_factor=1)
    # Local file access only. The sample is already published in this repository.
    page.goto(SOURCE.as_uri(), wait_until="load", timeout=30000)
    page.screenshot(path=str(OUT / "reconstruction-full-page.png"), full_page=True, animations="disabled")
    title = page.title()
    assert "реконструкция" in title.lower(), "Expected test-only, anonymized reconstruction"
    browser.close()
print("Screenshot smoke test passed (anonymized sample only; no Gmail access or publication).")
