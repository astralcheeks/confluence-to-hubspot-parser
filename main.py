from confluence_parser import parse_confluence_content
from get_confluence_content import get_confluence_content
from create_hubspot_page import create_hubspot_page
import config

# Parses input and returns a list of all page IDs to parse
def parse_input(user_input):
    return user_input.replace(" ", "").split(",")

# Main function to port Confluence page to Hubspot
def main():
    print("\nThis program ports a Confluence page to Hubspot.\n")
    user_input = input("Enter the Confluence ID of the page you want to port. For multiple page IDs, seperate them by comma (\'12345,67890\'): ")
    pages = parse_input(user_input)

    for page_id in pages:
        print(f"\nTreating page ID: {page_id}...")
        confluence_content, page_title = get_confluence_content(page_id=page_id)
        parsed_content, image_sources, image_filenames = parse_confluence_content(confluence_content, page_title)

        if parsed_content:
            create_hubspot_page(page_name=page_title,
                                template_path=config.template_path,
                                domain=config.domain,
                                slug='f{page_id}',
                                parsed_content=parsed_content,
                                page_title=page_title,
                                image_sources=image_sources,
                                image_filenames=image_filenames)
        
    print("\nAll pages processed. Goodbye!\n")

main()