import os
from bs4 import BeautifulSoup

# We can add more functions here as necessary

# Ex:

# def handle_warningbox()
# etc etc

def handle_infobox(main_soup):
    infoboxes = main_soup.find_all(class_="confluence-information-macro confluence-information-macro-information")
    for item in infoboxes:
        item['style'] = (
            "border-radius: var(--ds-border-radius, 3px);"
            "padding-top: var(--ds-space-100, 8px);"
            "padding-right: var(--ds-space-200, 16px);"
            "padding-bottom: var(--ds-space-100, 8px);"
            "padding-left: var(--ds-space-100, 8px);"
            "-webkit-align-items: normal;"
            "-webkit-box-align: normal;"
            "-ms-flex-align: normal;"
            "word-break: break-word;"
            "background-color: var(--ds-background-accent-blue-subtlest, #deebff);"
            "color: inherit;"
            "align-items: normal;"
            "min-width: 48px;"
            "margin: .75rem 0 0;"
            "display: -webkit-box;"
            "display: -webkit-flex;"
            "display: -ms-flexbox;"
            "display: flex;"
            "position:relative"
        )

# Handles expandable elements
def handle_expands(main_soup):
    expands = main_soup.find_all(class_='expand-container')
    expands_garbage = main_soup.find_all(class_='expand-control')

    for item in expands:
        item.name = "details"

    for item in expands_garbage:
        item.decompose()

def verify_overwrite(target_filepath, filename):
    if os.path.exists(target_filepath):
        user_input = input(f"Found a file already named \"{filename}\". Ok to overwrite? Type Y to proceed, or anything else to skip: ").strip().upper()
        if user_input == "Y":
            try:
                os.remove(target_filepath)
            except OSError as e:
                print(f"Error: {e.strerror}. Could not overwrite the file.")
                return False
        else: return False

    return True

# Makes necessary changes and parses html
def handle_content(main_soup, target_filepath):

    handle_expands(main_soup)
    handle_infobox(main_soup)

    with open(target_filepath, "a") as hubspot_page:
        hubspot_page.write(str(main_soup))

# Makes a soup from only the main page content, excluding all the other garbage Confluence puts in the export
def find_main_content(confluence_soup):
    main_content = confluence_soup.find('div', id='main-content')
    if main_content:
        return BeautifulSoup(main_content.prettify(), 'html.parser')
    else:
        return None

# Parses each file in the directory
def parse_files(files_to_parse, string_directory):
    for file in files_to_parse:
        source_path = os.path.join(string_directory, file)
        target_filepath = os.path.join(string_directory, "hubspot" + file)
        if verify_overwrite(target_filepath, file):
            try:
                with open(source_path, "r", encoding='utf-8') as confluence_page:
                    confluence_soup = BeautifulSoup(confluence_page.read(), 'html.parser')
                    main_soup = find_main_content(confluence_soup)
                    if main_soup:
                        handle_content(main_soup, target_filepath)
                        print(f"\nProcessed: {file}")
                    else:
                        print(f"Main content not found in: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

        else: continue

    print("\nDone! Your parsed files have been downloaded.\n")

# Asks user if they want to proceed to parse files
def validate_parse(files_to_parse):
    print("\nParse these files?\n")

    for file in files_to_parse:
        print(file)

    return input("\nType Y to proceed, or anything else to quit: \n").strip().upper() == "Y"

# Finds all valid files in directory
def get_files_to_parse(string_directory):
    try:
        return [
            filename for filename in os.listdir(string_directory)
            if filename.endswith(".html") and not filename.startswith("hubspot") and filename != "index.html"
        ]
    except FileNotFoundError:
        print(f"\nDirectory \"{string_directory}\" not found.\n")
    except PermissionError:
        print(f"\nWhoops! I don't have permission to access this directory.\n")

    return []

# Gets user input for directory to be used
def get_directory():
    while True:
        string_directory = input("\nEnter the directory absolute path below. Every html file in the directory will be parsed. \n")
        if os.path.isdir(string_directory):
            return string_directory
        else:
            print(f"Invalid directory: \"{string_directory}\". Please try again.")

# Main function
def main():
    print("\nThis program parses the HTML from Confluence docs for use in HubSpot.")

    string_directory = get_directory()
    files_to_parse = get_files_to_parse(string_directory)

    if files_to_parse and validate_parse(files_to_parse):
        parse_files(files_to_parse, string_directory) 
    elif not files_to_parse:
        print("\nNo parseable files found here.\n")

    print("Program finished.")

main()