import aiohttp
import config

# Confluence API credentials
confluence_username = config.confluence_username
confluence_api_token = config.confluence_api_token
confluence_base_url = config.confluence_base_url

async def get_confluence_content_async(session, page_id):
    url = f"{confluence_base_url}/rest/api/content/{page_id}?expand=body.export_view"
    auth = aiohttp.BasicAuth(confluence_username, confluence_api_token)
    headers = {'Accept': 'application/json'}
    async with session.get(url, headers=headers, auth=auth) as response:
        if response.status != 200:
            print(f"Failed to retrieve content from Confluence. Status code: {response.status}")
            return None, None, None
        confluence_data = await response.json()
        content = confluence_data['body']['export_view']['value']
        page_title = confluence_data['title']
        confluence_url = f"{confluence_base_url}/spaces/{confluence_data['_expandable']['space']}/pages/{page_id}"
        return content, page_title, confluence_url
