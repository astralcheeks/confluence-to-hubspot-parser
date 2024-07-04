import aiohttp
import json
import config

hubspot_access_token = config.hubspot_access_token
hubspot_base_url = config.hubspot_base_url

async def create_hubspot_page_async(session, page_name, template_path, domain, slug, parsed_content, page_title, state="DRAFT"):
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
    async with session.post(url, headers=headers, data=json.dumps(page_details)) as response:
        if response.status != 201:
            print(f"Failed to create page in HubSpot. Status code: {response.status}")
            return None, None
        response_data = await response.json()
        return response_data['id'], response_data['url']

async def update_hubspot_page_async(session, hubspot_page_id, updated_content):
    url = f"{hubspot_base_url}/cms/v3/pages/site-pages/{hubspot_page_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {hubspot_access_token}'
    }
    page_details = {
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
                                            "html": updated_content,
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
    }
    async with session.patch(url, headers=headers, data=json.dumps(page_details)) as response:
        if response.status != 200:
            print(f"Failed to update content for HubSpot page. Status code: {response.status}")
            return
        print(f"Successfully updated content for HubSpot page with ID {hubspot_page_id}")
