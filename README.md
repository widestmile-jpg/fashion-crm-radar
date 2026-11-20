# Fashion CRM Radar

Weekly competitive email marketing research. The public GitHub Pages site contains only deliberately published editorial material.

## Subscription-independent control

The GitHub repository and its Actions workflows can be used from the **Actions** tab without a ChatGPT plugin. This is a manual-review mode, not yet a production automated email-ingestion system.

### Screenshot test (safe)

1. Open **Actions → Fashion CRM Radar — test screenshot (no publishing)**.
2. Select **Run workflow**.
3. Download **fashion-radar-screenshot-smoke-test** from the completed run.

The test generates a full-page PNG of an **anonymized reconstruction already present in this public repository**. It does **not** access Gmail, render the original email, deliver mail, or change the published report.

### Publish an explicitly approved HTML issue

1. Review the candidate report located under `issues/` before publishing.
2. Open **Actions → Fashion CRM Radar — publish approved issue → Run workflow**.
3. Enter an exact `issue_path`, e.g. `issues/2026-10-29-final-review.html`.
4. Enter `PUBLISH_APPROVED` in the confirmation field.
5. Confirm the action run succeeded and verify the public site.

This operation **replaces `index.html`**. It does not send email and it does not create a draft. Do not run it until the report is genuinely approved. There is no schedule attached to this publication workflow.

## Production work not yet done

- **Gmail access:** configure OAuth for a dedicated, minimal-scope mailbox integration (or a dedicated forwarded-mailbox), with refresh-token rotation and secure secrets outside public Git. ChatGPT's Gmail plugin is *not* a durable credential for GitHub Actions.
- **Original rendering:** obtain actual HTML MIME parts and embedded/remote resources of opted-in competitor newsletters, sanitize potentially identifying tracking pixels and links, and test rendering with Playwright.
- **Privacy:** never commit raw emails, individual links, Gmail IDs, authorization tokens or private screenshots to this **public** repository. Public GitHub Actions artifacts and Pages should be treated as shareable. Store sensitive staging data in a separate private repository or suitably access-controlled storage.
- **Research:** de-duplicate by stable message identity, preserve campaign provenance, compare brands, and produce evidence-backed findings.
- **Private review:** create a draft for explicit approval *without deploying it to public Pages*; do not assume an unlisted public URL is private.
- **Email delivery:** connect a separate authorized sender and recipients; only send after explicit approval and guard against repeated delivery.
- **Scheduling:** schedule draft preparation only after the preceding components pass end-to-end tests. Do not automatically publish or email.

## Current safety status

The external ChatGPT Fashion CRM Radar scheduled task is paused. This repository has **no automated newsletter delivery**. The publishing workflow requires an explicit confirmation in GitHub Actions.
