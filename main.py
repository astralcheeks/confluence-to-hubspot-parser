import time
import asyncio
import aiohttp
import certifi
import ssl
from confluence_parser import parse_confluence_content, update_hyperlinks
from get_confluence_content import get_confluence_content_async
from create_hubspot_page import create_hubspot_page_async, update_hubspot_page_async, check_duplicate_titles

# Dictionary to map Confluence page IDs to HubSpot URLs and page IDs
url_mapping = {}
id_mapping = {}

def parse_input(user_input):
    return user_input.replace(" ", "").split(",")

async def fetch_confluence_page(session, page_id):
    print(f"\nRetrieving page ID: {page_id}...")
    confluence_content, page_title, confluence_url = await get_confluence_content_async(session, page_id=page_id)
    print(f"Found page: {page_title} (ID: {page_id})")
    return page_id, confluence_content, page_title, confluence_url

async def fetch_confluence_pages(pages):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = [fetch_confluence_page(session, page_id) for page_id in pages]
        confluence_data = await asyncio.gather(*tasks)
    return confluence_data

async def create_hubspot_page_task(session, page_id, parsed_content, page_title):
    print(f"Checking for duplicates for Confluence page ID: {page_id}")
    is_duplicate, existing_id, existing_url = await check_duplicate_titles(session, page_title)
    if is_duplicate:
        while True: 
            user_input = input(f"A page with the title '{page_title}' already exists in HubSpot. Do you want to create a duplicate? (yes/no): ")
            if user_input.lower() == 'no':
                print(f"Skipping creation of duplicate page for Confluence page ID: {page_id}")
                return page_id, existing_id, existing_url
            elif user_input == 'yes':
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'")

    print(f"Creating HubSpot page for Confluence page ID: {page_id}") 
    hubspot_id, hubspot_url = await create_hubspot_page_async(session, page_name=page_title,
                                                  template_path='/WebsitePagesTemplate.html',
                                                  domain='salmouradinc-46445795.hubspotpagebuilder.com',
                                                  slug=f'testpage-{page_id}',
                                                  parsed_content=parsed_content,
                                                  page_title=page_title,
                                                  state="PUBLISHED")  # Set state to PUBLISHED
    if hubspot_url:
        print(f"Created HubSpot page for Confluence page ID {page_id}: {hubspot_url}")
        return page_id, hubspot_id, hubspot_url
    return page_id, None, None

async def create_hubspot_pages(parsed_contents):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = [create_hubspot_page_task(session, page_id, parsed_content, page_title) 
                 for page_id, (parsed_content, page_title) in parsed_contents.items()]
        results = await asyncio.gather(*tasks)
        for page_id, hubspot_id, hubspot_url in results:
            if hubspot_url:
                url_mapping[page_id] = hubspot_url
                id_mapping[page_id] = hubspot_id
                print(f"HubSpot URL for Confluence page ID {page_id}: {hubspot_url}")

async def update_links(parsed_contents, hyperlinks):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = []
        for page_id, (parsed_content, page_title) in parsed_contents.items():
            if hyperlinks[page_id]:
                updated_content = update_hyperlinks(parsed_content, hyperlinks[page_id], url_mapping)
                print(f"Updating link from Confluence page ID {page_id} to HubSpot ID {id_mapping[page_id]}")
                parsed_contents[page_id] = (updated_content, page_title)
                tasks.append(update_hubspot_page_async(session, id_mapping[page_id], updated_content))
        await asyncio.gather(*tasks)

def process_confluence_pages(confluence_data):
    parsed_contents = {}
    hyperlinks = {}
    for page_id, confluence_content, page_title, confluence_url in confluence_data:
        parsed_content, links = parse_confluence_content(confluence_content)
        if parsed_content:
            parsed_contents[page_id] = (parsed_content, page_title)
            hyperlinks[page_id] = links
            print(f"Processed Confluence page ID {page_id}: found {len(links)} links")
    return parsed_contents, hyperlinks

async def main():
    print("\nThis program ports Confluence pages to Hubspot.\n")

    user_input = input("Enter the Confluence IDs of the pages you want to port. For multiple page IDs, separate them by comma ('12345,67890'): ")
    pages = parse_input(user_input)
    
    # Fetch Confluence pages
    confluence_data = await fetch_confluence_pages(pages)

    # Process Confluence pages
    parsed_contents, hyperlinks = process_confluence_pages(confluence_data)

    # Create HubSpot pages
    await create_hubspot_pages(parsed_contents)

    # Update links
    await update_links(parsed_contents, hyperlinks)

    # Verify that links have been updated correctly
    for page_id, (updated_content, page_title) in parsed_contents.items():
        if hyperlinks[page_id]:
            for link in hyperlinks[page_id]:
                if isinstance(link, dict) and 'url' in link:
                    original_url = link['url']
                    if original_url in url_mapping:
                        assert url_mapping[original_url] in updated_content, f"Link to {original_url} was not updated correctly in page {page_id}"
                        print(f"Verified link for {original_url} updated correctly in page {page_id}")



if __name__ == "__main__":
    asyncio.run(main())

print("Goodbye!")