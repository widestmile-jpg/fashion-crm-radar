/**
 * Fashion CRM Radar — safe browser-only Gmail read-only test.
 * Requires an Apps Script manifest with scopes gmail.readonly,
 * script.external_request; see scripts/apps-script-appsscript.json
 * Never prints message IDs, sender addresses or contents.
 */
function testFashionRadarGmail() {
  const response = UrlFetchApp.fetch(
    'https://gmail.googleapis.com/gmail/v1/users/me/messages?q=newer_than%3A7d&maxResults=5',
    {
      method: 'get',
      headers: {Authorization: 'Bearer ' + ScriptApp.getOAuthToken()},
      muteHttpExceptions: true
    }
  );
  if (response.getResponseCode() !== 200) {
    console.log('Gmail API check failed: HTTP ' + response.getResponseCode());
    throw new Error('Gmail read-only authorization failed. No email data was exported.');
  }
  const result = JSON.parse(response.getContentText());
  console.log('Gmail read-only access verified. At least one recent message: ' +
    Boolean(result.messages && result.messages.length));
  console.log('No email contents, senders, identifiers or attachments were saved or shared.');
}
