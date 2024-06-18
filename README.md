# Confluence to HubSpot Parser

This Python script ports a page from Confluence to HubSpot.

It retrieves the Confluence page HTML using the page ID, parses and tidies it up, and sends it to HubSpot to create a new page with that content.

Created for Summer 2024 technical writing internship.

## Setup

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

1. Download the project files:
    - Go to the [repository page](https://github.com/astralcheeks/confluence-to-hubspot-parser).
    - Click the green "Code" button.
    - Select "Download ZIP".
    - Extract the ZIP file to a directory of your choice.

2. Open a terminal (Command Prompt or PowerShell on Windows) and navigate to the project directory:
    ```sh
    cd path/to/your-repo
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Required Packages

- **Beautiful Soup**: Used for parsing HTML from Confluence.
- **Requests**: Used for making HTTP requests.


## API credentials
Before using the script, you will need to create a ```config.py``` file within the same directory.

In this file, define variables with your API credentials for both Confluence and HubSpot:

``` py
# Confluence API credentials
confluence_username = 'youremail@example.com'
confluence_api_token = 'api-token-here'
confluence_base_url = 'https://youraccount.atlassian.net/wiki'

# HubSpot API credentials
hubspot_access_token = 'access-token-here'
hubspot_base_url = 'https://api.hubspot.com'

# Library for HubSpot account
hubspot_library_url = 'https://youraccountnumber.fs1.hubspotusercontent-na1.net/hubfs/youraccountnumber/library'
```

Within the library URL, you can replace the path with any sub-folder you like to port page attachments there instead.

## Find Confluence Page ID

The script will prompt you for the ID of the page you want to port. You can find it in the page's URL:

https://example.atlassian.net/wiki/spaces/abcde12345/pages/67890/PageName

In this URL, **67890** is the page ID.