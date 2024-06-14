import requests
import json
import config

# HubSpot API credentials
hubspot_access_token = config.hubspot_access_token
hubspot_base_url = config.hubspot_base_url

# Creates a website page in HubSpot
def create_hubspot_page(page_name, template_path, domain, slug, parsed_content, page_title):
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
    else:
        print("\n\nFailed to create page.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)