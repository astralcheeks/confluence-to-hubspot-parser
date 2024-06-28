import requests
import json
import config

# HubSpot API credentials
hubspot_access_token = config.hubspot_access_token
hubspot_base_url = config.hubspot_base_url

class HubSpotClient:
    def __init__(self, access_token, base_url):
        self.access_token = access_token
        self.base_url = base_url

    def create_page(self, page_details):
        url = f"{self.base_url}/cms/v3/pages/site-pages"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }

        page_data = json.dumps(page_details)
        response = requests.post(url, headers=headers, data=page_data)
        return response

    def update_page_content(self, page_id, content):
        url = f"{self.base_url}/cms/v3/pages/site-pages/{page_id}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        
        # Modify layoutSections to include updated content
        layout_sections = {
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
                                            "html": content,
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
        }
        
        page_data = {
            'layoutSections': layout_sections
        }
        response = requests.patch(url, headers=headers, data=json.dumps(page_data))
        return response

    def get_page_content(self, page_id):
        url = f"{self.base_url}/cms/v3/pages/site-pages/{page_id}"
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = requests.get(url, headers)
        print(f"Get content response status code: {response.status_code}")
        print(f"Get content response content: {response.text}")
        return response

hubspot_client = HubSpotClient(hubspot_access_token, hubspot_base_url)

# Creates a website page in HubSpot
def create_hubspot_page(page_name, template_path, domain, slug, parsed_content, page_title, state="DRAFT"):
    print("Creating page in HubSpot...")
    page_details = {
        "name": page_name,
        "htmlTitle": page_title,
        "templatePath": template_path,
        "domain": domain,
        "slug": slug,
        "state": state,
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

    response = hubspot_client.create_page(page_details)

    if response.status_code == 201:
        print("\n\nPage created successfully.\n")
        created_page = response.json()
        hubspot_url = created_page['url']  # Capture the actual HubSpot URL
        return created_page['id'], hubspot_url
    else:
        print("\n\nFailed to create page.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return None, None

def update_hubspot_page(page_id, updated_content):
    response = hubspot_client.update_page_content(page_id, updated_content)
    if response.status_code == 200:
        print(f"Successfully updated content for HubSpot page with ID {page_id}")
    else:
        print(f"Failed to update content for HubSpot page with ID {page_id}")
        return None
