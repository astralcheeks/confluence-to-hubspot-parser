from bs4 import BeautifulSoup
import re

def cleanup_attributes(confluence_soup):
    return

def handle_info_panel(confluence_soup):
    infoboxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-information")
    for item in infoboxes:
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        info_icon = confluence_soup.new_tag("span")
        info_icon['data-hs-icon-hubl'] = "true"
        info_icon['style'] = "display: inline-block; fill: #2479f8; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"
        info_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"Circle Info\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Circle Info icon\" %} "
        
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        wrapper_div.append(info_icon)
        wrapper_div.append(text_content_div)
        
        item.clear()
        item.append(wrapper_div)

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
    notes_boxes = confluence_soup.find_all(class_="panel")
    for item in notes_boxes:
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        note_icon = confluence_soup.new_tag("span")
        note_icon['data-hs-icon-hubl'] = "true"
        note_icon['style'] = "display: inline-block; fill: #8270db; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"
        note_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"clipboard\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"clipboard\" %} "
        
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        wrapper_div.append(note_icon)
        wrapper_div.append(text_content_div)

        item.clear()
        item.append(wrapper_div)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: #f3f0fe;"
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )

        panel_contents = item.find_all(class_="panelContent")
        for panel_content in panel_contents:
            if 'style' in panel_content.attrs:
                styles = panel_content['style'].split(';')
                styles = [style for style in styles if 'background-color' not in style.strip()]
                panel_content['style'] = '; '.join(styles).strip('; ')
            else:
                panel_content['style'] = ''

    return confluence_soup

def handle_success_panel(confluence_soup):
    success_boxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-tip")
    for item in success_boxes:
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        success_icon = confluence_soup.new_tag("span")
        success_icon['data-hs-icon-hubl'] = "true"
        success_icon['style'] = "display: inline-block; fill: #2e7d32; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"
        success_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"Circle Check\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Check Circle icon\" %} "
        
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        wrapper_div.append(success_icon)
        wrapper_div.append(text_content_div)

        item.clear()
        item.append(wrapper_div)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: #dbfcf1;"
            "margin: .75rem 0 0;"
            "border-radius: var(--ds-border-radius,4px);"
        )

    return confluence_soup

def handle_warning_panel(confluence_soup):
    warning_boxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-note")
    for item in warning_boxes:
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        warning_icon = confluence_soup.new_tag("span")
        warning_icon['data-hs-icon-hubl'] = "true"
        warning_icon['style'] = "display: inline-block; fill: #ff9800; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"
        warning_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"triangle exclamation\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Exclamation Triangle icon\" %} "
        
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        wrapper_div.append(warning_icon)
        wrapper_div.append(text_content_div)

        item.clear()
        item.append(wrapper_div)

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
    error_boxes = confluence_soup.find_all(class_="confluence-information-macro confluence-information-macro-warning")
    for item in error_boxes:
        wrapper_div = confluence_soup.new_tag("div")
        wrapper_div['style'] = "display: flex; align-items: flex-start;"

        error_icon = confluence_soup.new_tag("span")
        error_icon['data-hs-icon-hubl'] = "true"
        error_icon['style'] = "display: inline-block; fill: #d32f2f; padding-right: 8px; padding-top: 16px; vertical-align: baseline;"
        error_icon.string = "{% icon icon_set=\"fontawesome-6.4.2\" name=\"circle xmark\" style=\"SOLID\" height=\"24\" purpose=\"decorative\" title=\"Times Circle icon\" %} "
        
        text_content_div = confluence_soup.new_tag("div")
        text_content_div['style'] = "flex: 1; display: inline-block;"

        for child in item.find_all(recursive=False):
            text_content_div.append(child.extract())

        wrapper_div.append(error_icon)
        wrapper_div.append(text_content_div)

        item.clear()
        item.append(wrapper_div)

        item['style'] = (
            "padding-top: 8px;"
            "padding-right: 16px;"
            "padding-bottom: 8px;"
            "padding-left: 8px;"
            "background-color: var(--ds-background-accent-red-subtlest, #FFEBE6);"
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


def handle_hyperlinks(confluence_soup):
    hyperlinks = {}
    for link in confluence_soup.find_all('a', href=True):
        href = link['href']
        confluence_page_id = link.get('data-linked-resource-id')
        if confluence_page_id:
            hyperlinks[confluence_page_id] = href
    return confluence_soup, hyperlinks

def handle_checkbox(confluence_soup):
    checkboxes = confluence_soup.find_all(class_="placeholder-inline-tasks")
    for checkbox in checkboxes:
        input_element = confluence_soup.new_tag("input", type="checkbox")
        if "checked" in checkbox.get("class", []):
            input_element["checked"] = "checked"
        
        # this just keeps the text next to the checkbox when porting
        checkbox_text = checkbox.get_text()

        # this keeps the checkbox and the text together
        span_element = confluence_soup.new_tag("span")
        span_element.append(input_element)
        span_element.append(checkbox_text)
        
        # changes checkbox placeholder with span element
        checkbox.replace_with(span_element)
    
    # Bullets kept showing in HubSpot when porting. This removes the bullets. 
    for ul in confluence_soup.find_all("ul", class_="inline-task-list"):
        ul["style"] = "list-style-type: none; padding: 0;"
        for li in ul.find_all("li"):
            li["style"] = "list-style-type: none; padding: 0;"

    return confluence_soup

def handle_tables(confluence_soup):
    tables = confluence_soup.find_all('table', class_='confluenceTable')
    for table in tables:
        table['style'] = "border-collapse: collapse; width: 100%;"
        
        # Process table headers
        headers = table.find_all('th', class_='confluenceTh')
        for header in headers:
            header_style = "border: 1px solid #ddd; padding: 8px; background-color: {};".format(header.get('data-highlight-colour', '#f2f2f2'))
            header['style'] = header_style
            header['style'] += "text-align: left;"

        # Process table cells
        cells = table.find_all('td', class_='confluenceTd')
        for cell in cells:
            cell_style = "border: 1px solid #ddd; padding: 8px;"
            cell['style'] = cell_style
            highlight_color = cell.get('data-highlight-colour')
            if highlight_color:
                cell['style'] += "background-color: {};".format(highlight_color)

    return confluence_soup

def handle_content(confluence_soup):
    confluence_soup = handle_expands(confluence_soup)
    confluence_soup = handle_info_panel(confluence_soup)
    confluence_soup = handle_note_panel(confluence_soup)
    confluence_soup = handle_success_panel(confluence_soup)
    confluence_soup = handle_warning_panel(confluence_soup)
    confluence_soup = handle_error_panel(confluence_soup)
    confluence_soup = handle_code_blocks(confluence_soup)
    confluence_soup = center_images(confluence_soup)
    confluence_soup, hyperlinks = handle_hyperlinks(confluence_soup)
    confluence_soup = handle_checkbox(confluence_soup) 
    confluence_soup = handle_tables(confluence_soup)

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

    return str(confluence_soup), hyperlinks

def parse_files(confluence_content):
    try:
        confluence_soup = BeautifulSoup(confluence_content, 'html.parser')
        print(f"Processing HTML...")
        return handle_content(confluence_soup)
    except Exception as e:
        print(f"Error processing: {e}")

def parse_confluence_content(confluence_content):
    if confluence_content:
        return parse_files(confluence_content) 
    else:
        print("\nNo parseable files found here.\n")
        return None, None
    
def update_hyperlinks(parsed_content, hyperlinks, url_mapping):
    soup = BeautifulSoup(parsed_content, 'html.parser')
    for confluence_page_id, href in hyperlinks.items():
        if confluence_page_id in url_mapping:
            new_href = url_mapping[confluence_page_id]
            for link in soup.find_all('a', attrs={'data-linked-resource-id': confluence_page_id}):
                print(f"Updating link from {href} to {new_href}")  # Debug print
                link['href'] = new_href
    updated_content = str(soup)
    return updated_content
