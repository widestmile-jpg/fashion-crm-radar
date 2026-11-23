/**
 * Fashion CRM Radar — safe browser-only Gmail connection test.
 *
 * Run within your own Google account in script.google.com.
 * This script only checks the number of recent threads.
 * It does NOT copy mail to GitHub, save messages, take screenshots or send anything.
 *
 * Note: GmailApp requires the broad Gmail OAuth permission (https://mail.google.com/),
 * even though this script only searches messages. Review Google's prompt carefully.
 */
function testFashionRadarGmail() {
  const query = 'newer_than:7d -in:spam -in:trash';
  const threads = GmailApp.search(query, 0, 5);
  const count = threads.length;
  console.log('Fashion CRM Radar: Gmail connection works. Found up to ' + count + ' recent threads.');
  console.log('No email content, message IDs, addresses or HTML were stored or exported.');
}
