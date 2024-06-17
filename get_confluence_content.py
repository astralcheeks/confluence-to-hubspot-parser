import requests
import config
import json

# Confluence API credentials
confluence_username = config.confluence_username
confluence_api_token = config.confluence_api_token
confluence_base_url = config.confluence_base_url

# Retrieves content from Confluence
def get_confluence_content(page_id):
    url = f"{confluence_base_url}/rest/api/content/{page_id}?expand=body.export_view"
    auth = (confluence_username, confluence_api_token)
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        confluence_data = response.json()
        content = confluence_data['body']['export_view']['value']
        page_title = confluence_data['title']
        print(f"\nFound page: {page_title}...")
        print(f"Retrieved content from Confluence...")
        return content, page_title
    else:
        print(f"Failed to retrieve content from Confluence. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None