import os
from bs4 import BeautifulSoup

# We can add more functions here as necessary

# Ex:

# def handle_infobox()
# def handle_warningbox()
# etc etc

# Handles expandable elements
def handle_expands(main_soup):
    expands = main_soup.find_all(class_='expand-container')
    expands_garbage = main_soup.find_all(class_='expand-control')

    for item in expands:
        item.name = "details"

    for item in expands_garbage:
        item.decompose()

# Makes necessary changes and parses html
def handle_content(main_soup, target_filename):
    with open(target_filename, "a") as hubspot_page:
        handle_expands(main_soup)
        hubspot_page.write(str(main_soup))

# Makes a soup from only the main page content, excluding all the other garbage Confluence puts in the export
def find_main_content(confluence_soup, target_filename):
   main_soup = BeautifulSoup(confluence_soup.find('div', id='main-content').prettify(), 'html.parser')
   handle_content(main_soup, target_filename)

# Parses each file in the directory
def parse_files(files_to_parse, string_directory):
    for file in files_to_parse:

        target_filename = string_directory + "hubspot" + file

        with open((string_directory + file), "r", encoding='utf-8') as confluence_page:
            confluence_soup = BeautifulSoup(confluence_page.read(), 'html.parser')
            find_main_content(confluence_soup, target_filename)

    print("\nDone! Your parsed files have been downloaded.\n")

# Asks user if they want to proceed to parse files
def validate_parse(files_to_parse):
    print("\nParse these files?\n")

    for file in files_to_parse:
        print(file)

    return True if input("\nType Y to proceed, or anything else to quit: ").upper() == "Y" else False

# Finds all valid files in directory
def get_files_to_parse(string_directory):
    files_to_parse = []
    try:
        for file in os.listdir(string_directory):
            filename = os.fsdecode(file)
            if filename.endswith(".html") and not filename.startswith("hubspot") and filename != "index.html":
                files_to_parse.append(filename)
    except FileNotFoundError:
        print(f"\nDirectory \"{string_directory}\" not found.\n")

    return files_to_parse

# Gets user input for directory to be used
def get_directory():
    while True:
        string_directory = input("\nEnter the directory absolute path below. Every html file in the directory will be parsed. \n")
        if not os.path.isdir(string_directory):
            print(f"Invalid directory: \"{string_directory}\". Please try again.")
        else:
            return string_directory

# Main function
def main():
    print("\nThis program parses the HTML from Confluence docs for use in HubSpot.")

    string_directory = get_directory()
    files_to_parse = get_files_to_parse(string_directory)

    if files_to_parse and validate_parse(files_to_parse):
        parse_files(files_to_parse, string_directory) 

    print("Program finished.")
    quit()

main()