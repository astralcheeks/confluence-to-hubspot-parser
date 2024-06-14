from confluence_parser import parse_confluence_content
from get_confluence_content import get_confluence_content
from create_hubspot_page import create_hubspot_page

def main():
    print("\nThis program ports a Confluence page to Hubspot.\n")
    page_id = input("Enter the Confluence ID of the page you want to port: ").strip()

    confluence_content, page_title = get_confluence_content(page_id=page_id)
    parsed_content = parse_confluence_content(confluence_content)

    if parsed_content:
        create_hubspot_page(page_name=page_title,
                            template_path='/templateTest.html',
                            domain='salmouradinc-46445795.hubspotpagebuilder.com',
                            slug='testpage',
                            parsed_content=parsed_content,
                            page_title=page_title)

main()