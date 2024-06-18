import requests
import json
import config
import os

# HubSpot API credentials
hubspot_access_token = config.hubspot_access_token
hubspot_base_url = config.hubspot_base_url

# Confluence API credentials
confluence_username = config.confluence_username
confluence_api_token = config.confluence_api_token
confluence_base_url = config.confluence_base_url

def download_image(file_url, filename):
    headers = {
        'Content-Type': 'application/json',
    }
    confluence_auth = (confluence_username, confluence_api_token)
    response = requests.get(file_url, headers=headers, auth=confluence_auth)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        return True
    else:
        print(f"Failed to download image: {filename}")
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        return False

# Uploads images for page
def upload_images(image_sources, image_filenames, page_title):
    headers = {
        'Authorization': f'Bearer {hubspot_access_token}',
    }
    url = f'{hubspot_base_url}/files/v3/files'
    folder_path = f'/library/docs_media/{page_title}'

    for i, file_url in enumerate(image_sources):
        filename = image_filenames[i]
        download_image(file_url, filename)
        files = {
            'file': open(filename, 'rb'),
            'folderPath': folder_path,
            'fileName': filename,
            'options': '{"access": "PUBLIC_INDEXABLE", "overwrite": "true"}'
        }
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 201:
            print(f"Page file uploaded succesfully: {filename}")
        else:
            print(f"Failed to upload image: {filename}")
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
        os.remove(filename)

    return

# Creates a website page in HubSpot
def create_hubspot_page(page_name, template_path, domain, slug, parsed_content, page_title, image_sources, image_filenames):
    print("Creating page in Hubspot...")
    url = f"{hubspot_base_url}/cms/v3/pages/site-pages"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {hubspot_access_token}'
    }

    page_details = {
        "name": page_name,
        "htmlTitle": page_title,
        "templatePath": template_path,
        "domain": domain,
        "slug": slug,
        "state": "DRAFT",
        "layoutSections": {
        "dnd_area": {
            "cells": [],
            "cssClass": "",
            "cssId": "",
            "cssStyle": "",
            "label": "Main section",
            "name": "dnd_area",
            "params": {},
            "rowMetaData": [
                {
                    "cssClass": "dnd-section"
                }
            ],
            "rows": [
                {
                    "0": {
                        "cells": [],
                        "cssClass": "",
                        "cssId": "",
                        "cssStyle": "",
                        "name": "cell_17182846336062",
                        "params": {
                            "css_class": "dnd-column"
                        },
                        "rowMetaData": [
                            {
                                "cssClass": "dnd-row"
                            }
                        ],
                        "rows": [
                            {
                                "0": {
                                    "cells": [],
                                    "cssClass": "",
                                    "cssId": "",
                                    "cssStyle": "",
                                    "label": "Rich Text",
                                    "name": "widget_1718284633457",
                                    "params": {
                                        "css_class": "dnd-module",
                                        "html": parsed_content,
                                        "module_id": 1155639,
                                        "schema_version": 2
                                    },
                                    "rowMetaData": [],
                                    "rows": [],
                                    "type": "custom_widget",
                                    "w": 12,
                                    "x": 0
                                }
                            }
                        ],
                        "type": "cell",
                        "w": 12,
                        "x": 0
                    }
                }
            ],
            "type": "cell",
            "w": 12,
            "x": 0
        }
    },
    }

    page_data = json.dumps(page_details)
    response = requests.post(url, headers=headers, data=page_data)

    if response.status_code == 201:
        print("\n\nPage created successfully.\n")
        upload_images(image_sources, image_filenames, page_title)
    else:
        print("\n\nFailed to create page.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)