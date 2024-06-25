from confluence_parser import parse_confluence_content
from get_confluence_content import get_confluence_content
from create_hubspot_page import create_hubspot_page

def parse_input(user_input):
    return user_input.replace(" ", "").split(",")

def main():
    print("\nThis program ports a Confluence page to Hubspot.\n")
    user_input = input("Enter the Confluence ID of the page you want to port. For multiple page IDs, seperate them by comma (\'12345,67890\'): ")
    pages = parse_input(user_input)

    for page_id in pages:
        print(f"\nTreating page ID: {page_id}...")
        confluence_content, page_title = get_confluence_content(page_id=page_id)
        parsed_content = parse_confluence_content(confluence_content)

        if parsed_content:
            create_hubspot_page(page_name=page_title,
                                template_path='/MainTempalte.html',
                                domain='salmouradinc-46445795.hubspotpagebuilder.com',
                                slug='testpage',
                                parsed_content=parsed_content,
                                page_title=page_title)
        
    print("\nAll pages processed. Goodbye!\n")

main()

