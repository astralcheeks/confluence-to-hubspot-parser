from bs4 import BeautifulSoup

# We can add more functions here as necessary

# Ex:

# def handle_warningbox()
# etc etc

# For every tag, removes garbage attributes that are not needed in HubSpot
def cleanup_attributes(confluence_soup):
    return

def handle_info_panel(confluence_soup):
    infoboxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-information")
    for item in infoboxes:
        # Create a wrapper div
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        # Create the info icon span
        info_icon = confluence_soup.new_tag("span")
        info_icon['data-hs-icon-hubl'] = "true"
        info_icon['style'] = "display: inline-block; fill: #2479f8; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"
        info_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"Circle Info\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Circle Info icon\" %} "
        
        # Create the text content div
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        # Move all children of the item to the text content div
        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        # Append the info icon and text content div to the wrapper div
        wrapper_div.append(info_icon)
        wrapper_div.append(text_content_div)
        
        # Replace the original item content with the wrapper div
        item.clear()
        item.append(wrapper_div)

        # Apply the styling to the item
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
    for item in notes_boxes:
        # Create a wrapper div
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        # Create the note icon span
        note_icon = confluence_soup.new_tag("span")
        note_icon['data-hs-icon-hubl'] = "true"
        note_icon['style'] = "display: inline-block; fill: #8270db; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"  # Purple color
        note_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"clipboard\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"clipboard\" %} "
        
        # Create the text content div
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        # Move all children of the item to the text content div
        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        # Append the note icon and text content div to the wrapper div
        wrapper_div.append(note_icon)
        wrapper_div.append(text_content_div)

        # Replace the original item content with the wrapper div
        item.clear()
        item.append(wrapper_div)

        # Apply the styling to the item
        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: #f3f0fe;"  # Light purple background
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )

        # Remove background color from panelContent
        panel_contents = item.find_all(class_="panelContent")
        for panel_content in panel_contents:
            if 'style' in panel_content.attrs:
                # Remove background color style if it exists
                styles = panel_content['style'].split(';')
                styles = [style for style in styles if 'background-color' not in style.strip()]
                panel_content['style'] = '; '.join(styles).strip('; ')
            else:
                # Ensure there is no background color
                panel_content['style'] = ''

    return confluence_soup


def handle_success_panel(confluence_soup):
    # Handle success panel boxes
    success_boxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-tip")
    for item in success_boxes:
        # Create a wrapper div
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        # Create the success icon span
        success_icon = confluence_soup.new_tag("span")
        success_icon['data-hs-icon-hubl'] = "true"
        success_icon['style'] = "display: inline-block; fill: #2e7d32; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"  # Green color
        success_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"Circle Check\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Check Circle icon\" %} "
        
        # Create the text content div
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        # Move all children of the item to the text content div
        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        # Append the success icon and text content div to the wrapper div
        wrapper_div.append(success_icon)
        wrapper_div.append(text_content_div)

        # Replace the original item content with the wrapper div
        item.clear()
        item.append(wrapper_div)

        # Apply the styling to the item
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
        # Create a wrapper div
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        # Create the warning icon span
        warning_icon = confluence_soup.new_tag("span")
        warning_icon['data-hs-icon-hubl'] = "true"
        warning_icon['style'] = "display: inline-block; fill: #ff9800; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"  # Orange color
        warning_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"triangle exclamation\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Exclamation Triangle icon\" %} "
        
        # Create the text content div
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        # Move all children of the item to the text content div
        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        # Append the warning icon and text content div to the wrapper div
        wrapper_div.append(warning_icon)
        wrapper_div.append(text_content_div)

        # Replace the original item content with the wrapper div
        item.clear()
        item.append(wrapper_div)

        # Apply the styling to the item
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
        # Create a wrapper div
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        # Create the error icon span
        error_icon = confluence_soup.new_tag("span")
        error_icon['data-hs-icon-hubl'] = "true"
        error_icon['style'] = "display: inline-block; fill: #d32f2f; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"  # Red color
        error_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"circle xmark\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Times Circle icon\" %} "
        
        # Create the text content div
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        # Move all children of the item to the text content div
        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        # Append the error icon and text content div to the wrapper div
        wrapper_div.append(error_icon)
        wrapper_div.append(text_content_div)

        # Replace the original item content with the wrapper div
        item.clear()
        item.append(wrapper_div)

        # Apply the styling to the item
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

def handle_code_blocks(confluence_soup):
    code_blocks = confluence_soup.find_all('code')
    for code in code_blocks:
        code['style'] = "background-color: #F4F5F7; padding: 0.2em 0.4em; border-radius: 0.3em;"

    return confluence_soup

# Makes necessary changes and parses html
def handle_content(confluence_soup):

    confluence_soup = handle_expands(confluence_soup)
    confluence_soup = handle_info_panel(confluence_soup)
    confluence_soup = handle_note_panel(confluence_soup)
    confluence_soup = handle_success_panel(confluence_soup)
    confluence_soup = handle_warning_panel(confluence_soup)
    confluence_soup = handle_error_panel(confluence_soup)
    confluence_soup = handle_code_blocks(confluence_soup)
    confluence_soup = center_images(confluence_soup)


    # Add CSS for Times New Roman font and text indentation
    style_tag = confluence_soup.new_tag("style")
    style_tag.string = """
        body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 1.2em;
        }
    """

    if confluence_soup.head:
        confluence_soup.head.insert(0, style_tag)
    else:
        head_tag = confluence_soup.new_tag("head")
        head_tag.insert(0, style_tag)
        confluence_soup.insert(0, head_tag)


    return str(confluence_soup)

# Parses each file in the directory
def parse_files(confluence_content):
    try:
        confluence_soup = BeautifulSoup(confluence_content, 'html.parser')
        print(f"Processing HTML...")
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