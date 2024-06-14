from bs4 import BeautifulSoup

# We can add more functions here as necessary

# Ex:

# def handle_warningbox()
# etc etc

# For every tag, removes garbage attributes that are not needed in HubSpot
def cleanup_attributes(confluence_soup):
    return

# Handle infoboxes
def handle_infobox(confluence_soup):
    infoboxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-information")
    for item in infoboxes:
        info_icon = confluence_soup.new_tag("span")
        info_icon['data-hs-icon-hubl'] = "true"
        info_icon['style'] = "display: inline-block; fill: #33475b;"
        info_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"Circle Info\"\
                            style=\"SOLID\" height=\"14\" purpose=\"decorative\" title=\"Circle Info icon\" %} "
        item.p.insert(0, info_icon)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: var(--ds-background-accent-blue-subtlest, #deebff);"
            "margin: .75rem 0 0;"
        )

    return confluence_soup

# Handles expandable elements
def handle_expands(confluence_soup):
    expands = confluence_soup.find_all(class_='expand-container')
    expands_garbage = confluence_soup.find_all(class_='expand-control')

    for item in expands:
        item.name = "details"
        
        summary = confluence_soup.new_tag("summary")
        summary.string = "More info"
        item.insert(0, summary)

    for item in expands_garbage: 
        item.decompose()

    return confluence_soup

# Makes necessary changes and parses html
def handle_content(confluence_soup):

    confluence_soup = handle_expands(confluence_soup)
    confluence_soup = handle_infobox(confluence_soup)

    return str(confluence_soup)

# Parses each file in the directory
def parse_files(confluence_content):
    try:
        confluence_soup = BeautifulSoup(confluence_content, 'html.parser')
        print(f"Processing html...")
        return handle_content(confluence_soup)
    except Exception as e:
        print(f"Error processing: {e}")

# Main function
def parse_confluence_content(confluence_content):
    if confluence_content:
        return parse_files(confluence_content) 
    else:
        print("\nNo parseable files found here.\n")
        return None