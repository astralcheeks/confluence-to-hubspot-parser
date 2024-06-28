# confluence-to-hubspot-parser

Python script to port a page from Confluence to Hubspot. Gets Confluence page HTML by the page ID, parses and tidies it up, and sends it to HubSpot to create a new page with that content.

Created for summer 2024 technical writing internship.

---------------------------------------------------------------------------------------------------

<h2>Find Confluence Page ID:</h2>
To find the Confluence page ID, refer to the Confluence page URL. The ID will be embedded in the URL. Here’s an example:

https://salmourad.atlassian.net/wiki/spaces/~71202049bafe525bfa4d8c8190c1a374ba76ff/pages/65677/test+123

In this URL, 65677 is the page ID.

---------------------------------------------------------------------------------------------------
<h2>Preserving Hyperlinks Between Pages</h2>
To maintain the hyperlink relationships between pages when porting from Confluence to HubSpot, you must ensure that you port both the document that contains the hyperlink and the document it links to together. If you port a document with a hyperlink before porting the linked document, the hyperlinks will not persist.

<h3>Example:</h3>
Consider two documents in Confluence:

Document A contains a hyperlink to Document B.
<br></br>
To preserve the hyperlink between Document A and Document B during the porting process ensure both Document A and Document B are ported together by entering in both their ID's when prompted by the program. 



