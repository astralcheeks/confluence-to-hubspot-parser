from bs4 import BeautifulSoup
import config

# We can add more functions here as necessary

# Ex:

# def handle_warningbox()
# etc etc

# For every tag, removes garbage attributes that are not needed in HubSpot
def cleanup_attributes(confluence_soup):
    return

def handle_images(confluence_soup, page_title):
    image_tags = confluence_soup.find_all(class_="confluence-embedded-file-wrapper")
    image_sources = []
    image_filenames = []

    for tag in image_tags:
        image_sources.append(tag.img['src'])
        image_filenames.append(tag.img['alt'])
        tag.img['src'] = f"{config.hubspot_library_url}/{page_title}/{tag.img['alt']}"

    return image_sources, image_filenames

# Handle infoboxes
def handle_info_panel(confluence_soup):
    infoboxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-information")
    for item in infoboxes:
        info_icon = confluence_soup.new_tag("span")
        info_icon['data-hs-icon-hubl'] = "true"
        info_icon['style'] = "display: inline-block; fill: #2479f8; padding-right: 8px; vertical-align: middle;"
        info_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"Circle Info\"\
                            style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Circle Info icon\" %} "
        item.p.insert(0, info_icon)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: var(--ds-background-accent-blue-subtlest, #deebff);"
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )

    return confluence_soup

def handle_note_panel(confluence_soup):
    # Handle notes panel boxes
    notes_boxes = confluence_soup.find_all(class_="panel")
    panel_contents = confluence_soup.find_all(class_="panelContent")
    for item in notes_boxes:
        note_icon = confluence_soup.new_tag("span")
        note_icon['data-hs-icon-hubl'] = "true"
        note_icon['style'] = "display: inline-block; fill: #8270db; padding-right: 8px; vertical-align: middle;"  # Purple color
        # Specify the correct icon name and check if "Memo" is available in your Font Awesome version
        note_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"clipboard\" \
                            style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"clipboard\" %} "
        item.p.insert(0, note_icon)
    
    for panel_content in panel_contents:
        if 'style' in panel_content.attrs:
            # Spliting the style attr into individual styles
            styles = panel_content['style'].split(';')
            # remove the unwatned background color
            styles = [style for style in styles if 'background-color' not in style.strip()]
            # remake the style attrb
            panel_content['style'] = '; '.join(styles).strip('; ')

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: #f3f0fe;"  # Light purple background
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )
    return confluence_soup

def handle_success_panel(confluence_soup):
    # Handle success panel boxes
    success_boxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-tip")
    for item in success_boxes:
        success_icon = confluence_soup.new_tag("span")
        success_icon['data-hs-icon-hubl'] = "true"
        success_icon['style'] = "display: inline-block; fill: #2e7d32; padding-right: 8px; vertical-align: middle;"  # Green color
        success_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"Circle Check\"\
                            style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Check Circle icon\" %} "
        item.p.insert(0, success_icon)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: #dbfcf1;"  # Light green background
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )
    return confluence_soup

def handle_warning_panel(confluence_soup):
    # Handle warning panel boxes
    warning_boxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-note")
    for item in warning_boxes:
        warning_icon = confluence_soup.new_tag("span")
        warning_icon['data-hs-icon-hubl'] = "true"
        warning_icon['style'] = "display: inline-block; fill: #ff9800; padding-right: 8px; vertical-align: middle;"  # Orange color
        warning_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"triangle exclamation\"\
                            style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Exclamation Triangle icon\" %} "
        
        item.p.insert(0, warning_icon)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: var(--ds-background-accent-yellow-subtlest, #fffae6);"
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )
    return confluence_soup

def handle_error_panel(confluence_soup):
    # Handle error panel boxes
    error_boxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-warning")
    for item in error_boxes:
        error_icon = confluence_soup.new_tag("span")
        error_icon['data-hs-icon-hubl'] = "true"
        error_icon['style'] = "display: inline-block; fill: #d32f2f; padding-right: 8px; vertical-align: middle;"  # Red color
        error_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"circle xmark\"\
                            style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Times Circle icon\" %} "
        item.p.insert(0, error_icon)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: var(--ds-background-accent-red-subtlest, #FFEBE6);"  # Light red background
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )
    return confluence_soup

# Handles expandable elements
def handle_expands(confluence_soup):
    expands = confluence_soup.find_all(class_='expand-container')
    expands_garbage = confluence_soup.find_all(class_='expand-control')

    for item in expands:
        item.name = "details"
        item['style'] = 'border: 1px solid #ccc; display: block; padding: 8px; border-radius: 5px'

        # create summary tag
        summary = confluence_soup.new_tag("summary")
        summary.string = "More info"
        item.insert(0, summary)

    for item in expands_garbage: 
        item.decompose()

    return confluence_soup

# Function to center images using CSS
def center_images(confluence_soup):
    images = confluence_soup.find_all('img')
    for img in images:
        img['style'] = "display: block; margin: 0 auto; border: 3px solid #ccc; padding: 5px; margin-bottom: 30px;" 

    return confluence_soup

# Makes necessary changes and parses html
def handle_content(confluence_soup, page_title):

    confluence_soup = handle_expands(confluence_soup)
    confluence_soup = handle_info_panel(confluence_soup)
    confluence_soup = handle_note_panel(confluence_soup)
    confluence_soup = handle_success_panel(confluence_soup)
    confluence_soup = handle_warning_panel(confluence_soup)
    confluence_soup = handle_error_panel(confluence_soup)
    confluence_soup = center_images(confluence_soup)
    image_sources, image_filenames = handle_images(confluence_soup, page_title)

    # Add CSS for Times New Roman font and text indentation
    style_tag = confluence_soup.new_tag("style")
    style_tag.string = """
        body {
            font-family: helvetica, sans-serif;
            font-size: 1.2em;
        }
    """

    if confluence_soup.head:
        confluence_soup.head.insert(0, style_tag)
    else:
        head_tag = confluence_soup.new_tag("head")
        head_tag.insert(0, style_tag)
        confluence_soup.insert(0, head_tag)


    return str(confluence_soup), image_sources, image_filenames

# Parses each file in the directory
def parse_files(confluence_content, page_title):
    try:
        confluence_soup = BeautifulSoup(confluence_content, 'html.parser')
        print(f"Processing HTML...")
        return handle_content(confluence_soup, page_title)
    except Exception as e:
        print(f"Error processing: {e}")

# Main function
def parse_confluence_content(confluence_content, page_title):
    if confluence_content:
        return parse_files(confluence_content, page_title) 
    else:
        print("\nNo parseable files found here.\n")
        return None