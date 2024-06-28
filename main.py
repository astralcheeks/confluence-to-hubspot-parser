from confluence_parser import parse_confluence_content, update_hyperlinks
from get_confluence_content import get_confluence_content
from create_hubspot_page import create_hubspot_page, update_hubspot_page

# Dictionary to map Confluence page IDs to HubSpot URLs and page IDs
url_mapping = {}
id_mapping = {}

def parse_input(user_input):
    return user_input.replace(" ", "").split(",")

def main():
    print("\nThis program ports Confluence pages to Hubspot.\n")
    user_input = input("Enter the Confluence IDs of the pages you want to port. For multiple page IDs, separate them by comma ('12345,67890'): ")
    pages = parse_input(user_input)

    confluence_data = []
    for page_id in pages:
        print(f"\nRetrieving page ID: {page_id}...")
        confluence_content, page_title, confluence_url = get_confluence_content(page_id=page_id)
        if confluence_content:
            confluence_data.append((page_id, confluence_content, page_title, confluence_url))

    # Parse all documents and collect hyperlinks
    parsed_contents = {}
    hyperlinks = {}
    for page_id, confluence_content, page_title, confluence_url in confluence_data:
        parsed_content, links = parse_confluence_content(confluence_content)
        if parsed_content:
            parsed_contents[page_id] = (parsed_content, page_title)
            hyperlinks[page_id] = links

    # Create HubSpot pages and store their URLs
    for page_id, (parsed_content, page_title) in parsed_contents.items():
        hubspot_id, hubspot_url = create_hubspot_page(page_name=page_title,
                                                      template_path='/WebsitePagesTemplate.html',
                                                      domain='salmouradinc-46445795.hubspotpagebuilder.com',
                                                      slug=f'testpage-{page_id}',
                                                      parsed_content=parsed_content,
                                                      page_title=page_title,
                                                      state="PUBLISHED")  # Set state to PUBLISHED
        if hubspot_url:
            url_mapping[page_id] = hubspot_url
            id_mapping[page_id] = hubspot_id
            print(f"HubSpot URL for Confluence page ID {page_id}: {hubspot_url}")

    # Update hyperlinks with actual HubSpot URLs
    for page_id, (parsed_content, page_title) in parsed_contents.items():
        if hyperlinks[page_id]:
            updated_content = update_hyperlinks(parsed_content, hyperlinks[page_id], url_mapping)
            parsed_contents[page_id] = (updated_content, page_title)

    # Update the HubSpot pages with updated content
    for page_id, (updated_content, page_title) in parsed_contents.items():
        if page_id in id_mapping:
            update_hubspot_page(id_mapping[page_id], updated_content)

    print("\nAll pages processed. Goodbye!\n")

if __name__ == "__main__":
    main()
