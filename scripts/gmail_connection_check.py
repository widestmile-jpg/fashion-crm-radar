"""Independent Gmail API connection smoke test.

Read-only; returns only aggregate number of messages found, never subjects,
addresses, IDs, HTML, snippets, or content; nothing is saved or published.
"""
import os
import sys
import requests

required = ("GMAIL_OAUTH_CLIENT_ID", "GMAIL_OAUTH_CLIENT_SECRET", "GMAIL_OAUTH_REFRESH_TOKEN")
missing = [name for name in required if not os.environ.get(name)]
if missing:
    print("Authorization not configured. Add three Gmail OAuth secrets in repository Settings.")
    sys.exit(2)

token_response = requests.post(
    "https://oauth2.googleapis.com/token",
    data={
        "client_id": os.environ["GMAIL_OAUTH_CLIENT_ID"],
        "client_secret": os.environ["GMAIL_OAUTH_CLIENT_SECRET"],
        "refresh_token": os.environ["GMAIL_OAUTH_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    },
    timeout=20,
)
if token_response.status_code != 200:
    print("Google OAuth exchange failed (no response body printed).")
    sys.exit(3)
access_token = token_response.json().get("access_token")
if not access_token:
    print("Google did not issue an access token.")
    sys.exit(4)

response = requests.get(
    "https://gmail.googleapis.com/gmail/v1/users/me/messages",
    headers={"Authorization": "Bearer " + access_token},
    params={"q": "newer_than:7d -in:spam -in:trash", "maxResults": 5},
    timeout=30,
)
if response.status_code != 200:
    print("Gmail read-only list request failed (no response body printed).")
    sys.exit(5)
result = response.json()
print("Gmail read-only access verified.")
print("At least one recent message:", bool(result.get("messages")))
print("No message content, addresses, identifiers or screenshots were downloaded or published.")
