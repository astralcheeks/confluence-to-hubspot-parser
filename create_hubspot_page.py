import requests
import json

# HubSpot API credentials
hubspot_access_token = 'hubspot_access_token'
hubspot_base_url = 'hubspot_base_url'

# Creates a website page in HubSpot
def create_hubspot_page(page_name, template_path, domain, slug, parsed_content):
    url = f"{hubspot_base_url}/cms/v3/pages/site-pages"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {hubspot_access_token}'
    }

    page_details = {
        "name": page_name,
        "templatePath": template_path,
        "domain": domain,
        "slug": slug,
        "state": "DRAFT",
        "layoutSections": {
        "dnd_area": {
            "label": "Main section",
            "name": "dnd_area",
            "rows": [
                {
                    "0": {
                        "label": "Rich Text",
                        "name": "widget_1718284633457",
                        "params": {
                            "css_class": "dnd-module",
                            "html": parsed_content,
                            "module_id": 1155639,
                        },
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
    },
    }

    page_data = json.dumps(page_details)
    response = requests.post(url, headers=headers, data=page_data)

    if response.status_code == 201:
        print("Page created successfully.")
    else:
        print("Failed to create page.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)