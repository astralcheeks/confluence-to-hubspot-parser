import requests
import json

# Confluence API credentials
confluence_username = 'confluence_username'
confluence_api_token = 'confluence_api_token'
confluence_base_url = 'confluence_base_url'

# Retrieves content from Confluence
def get_confluence_content(page_id):
    url = f"{confluence_base_url}/rest/api/content/{page_id}?expand=body.export_view"
    auth = (confluence_username, confluence_api_token)
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers, auth=auth)
    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        confluence_data = response.json()
        content = confluence_data['body']['export_view']['value']

        with open("confluence_page.html", 'w') as test_file:
            test_file.write(content)

        print(f"Retrieved content from Confluence...")
        return content
    else:
        print(f"Failed to retrieve content from Confluence. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None