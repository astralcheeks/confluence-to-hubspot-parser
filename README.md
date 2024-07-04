# confluence-to-hubspot-parser


This program is designed to make it easy to transfer Confluence pages to HubSpot. It handles various components and features, saving you time and effort compared to manual copying. Here are the key functionalities:

1. Fetching Confluence Pages
<ul>
  <li><strong>Fetches Multiple Pages:</strong> Quickly retrieves multiple Confluence pages at once.</li>
  <li><strong>Error Handling:</strong> Provides feedback if there's an issue retrieving content.</li>
</ul>
2. Processing Confluence Content
<ul>
  <li><strong>HTML Parsing and Cleaning:</strong> Cleans and organizes the HTML content from Confluence.</li>
  <li><strong>Handling Various Panels:</strong>
    <ul>
      <li><strong>Info Panels:</strong> Converts Confluence information panels to a format suitable for HubSpot.</li>
      <li><strong>Note Panels:</strong> Converts Confluence note panels, including icons and styles.</li>
      <li><strong>Success Panels:</strong> Converts Confluence success panels with appropriate styling and icons.</li>
      <li><strong>Warning Panels:</strong> Converts Confluence warning panels with cautionary icons and styles.</li>
      <li><strong>Error Panels:</strong> Converts Confluence error panels to ensure important information stands out.</li>
    </ul>
  </li>
  <li><strong>Handling Expands:</strong> Converts expandable sections in Confluence to collapsible sections in HTML.</li>
  <li><strong>Centering Images:</strong> Ensures images are centered and styled with borders and padding.</li>
  <li><strong>Styling Code Blocks:</strong> Applies background color and padding to code blocks to enhance readability.</li>
</ul>
3. Creating HubSpot Pages
<ul>
  <li><strong>Creates HubSpot Pages:</strong> Automatically creates new HubSpot pages using the content from Confluence.</li>
  <li><strong>Template Integration:</strong> Uses predefined templates for consistent page design.</li>
  <li><strong>Dynamic Content Insertion:</strong> Inserts cleaned and formatted content into HubSpot pages.</li>
</ul>
4. Updating Hyperlinks
<ul>
  <li><strong>Hyperlink Mapping:</strong> Updates internal links to point to the new HubSpot pages.</li>
</ul>

---------------------------------------------------------------------------------------------------
<h1>How to Use</h1>

<h3>Find Confluence Page ID</h3>
<p>To find the Confluence page ID, refer to the Confluence page URL. The ID will be embedded in the URL. Here’s an example:</p>
<pre>
https://salmourad.atlassian.net/wiki/spaces/~71202049bafe525bfa4d8c8190c1a374ba76ff/pages/65677/test+123
</pre>
<p>In this URL, <code>65677</code> is the page ID.</p>

<hr>

<h3>Preserving Hyperlinks Between Pages</h3>
<p>To maintain the hyperlink relationships between pages when porting from Confluence to HubSpot, you must ensure that you port both the document that contains the hyperlink and the document it links to together. If you port a document with a hyperlink before porting the linked document, the hyperlinks will not persist.</p>

<h4>Example:</h4>
<p>Consider two documents in Confluence:</p>
<ul>
  <li>Document A contains a hyperlink to Document B.</li>
</ul>
<p>To preserve the hyperlink between Document A and Document B during the porting process, ensure both Document A and Document B are ported together by entering both their IDs when prompted by the program. This ensures that Document A in HubSpot is linked to Document B in HubSpot.</p>

<hr>

