from typing import List, Dict
import re
import json
from bs4 import BeautifulSoup

def extract_form_ids(html_content: str) -> List[str]:
    """Extract all form input IDs from the HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    form_ids = set()
    
    # Find the FB_PUBLIC_LOAD_DATA_ variable
    script_tags = soup.find_all('script')
    print(f"Found {len(script_tags)} script tags")
    
    for script in script_tags:
        if script.string and 'FB_PUBLIC_LOAD_DATA_' in script.string:
            print("Found FB_PUBLIC_LOAD_DATA_ in script")
            # Extract the JSON data
            match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(\[.*?\]);', script.string, re.DOTALL)
            if match:
                print("Successfully matched regex pattern")
                try:
                    json_str = match.group(1)
                    print(f"Extracted JSON string: {json_str[:200]}...")
                    data = json.loads(json_str)
                    print(f"Successfully parsed JSON. Data structure: {type(data)}")
                    
                    # Form fields are in data[1][1]
                    if len(data) > 1 and len(data[1]) > 1:
                        form_fields = data[1][1]
                        print(f"Found {len(form_fields)} form fields")
                        for field in form_fields:
                            if isinstance(field, list) and len(field) > 4:
                                field_id = field[0]
                                field_type = field[3]
                                # Check if there are nested fields
                                if len(field) > 4 and isinstance(field[4], list):
                                    for nested_field in field[4]:
                                        if isinstance(nested_field, list) and len(nested_field) > 0:
                                            nested_id = nested_field[0]
                                            if isinstance(nested_id, int):
                                                form_ids.add(f"entry.{nested_id}")
                                                if field_type == 10:  # Time input
                                                    form_ids.add(f"entry.{nested_id}_hour")
                                                    form_ids.add(f"entry.{nested_id}_minute")
                                                elif field_type == 9:  # Date input
                                                    form_ids.add(f"entry.{nested_id}_year")
                                                    form_ids.add(f"entry.{nested_id}_month")
                                                    form_ids.add(f"entry.{nested_id}_day")
                                else:
                                    form_ids.add(f"entry.{field_id}")
                                    if field_type == 10:  # Time input
                                        form_ids.add(f"entry.{field_id}_hour")
                                        form_ids.add(f"entry.{field_id}_minute")
                                    elif field_type == 9:  # Date input
                                        form_ids.add(f"entry.{field_id}_year")
                                        form_ids.add(f"entry.{field_id}_month")
                                        form_ids.add(f"entry.{field_id}_day")
                except (json.JSONDecodeError, IndexError) as e:
                    print(f"Error processing data: {str(e)}")
                    continue
    
    print(f"\nExtracted form IDs: {sorted(form_ids)}")
    return list(form_ids)

def extract_form_ids_and_labels(html_content: str) -> Dict[str, str]:
    """Extract form input IDs and their corresponding labels"""
    soup = BeautifulSoup(html_content, 'html.parser')
    form_mapping = {}
    
    # Find the FB_PUBLIC_LOAD_DATA_ variable
    script_tags = soup.find_all('script')
    
    for script in script_tags:
        if script.string and 'FB_PUBLIC_LOAD_DATA_' in script.string:
            # Extract the JSON data
            match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(\[.*?\]);', script.string, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group(1))
                    
                    # Form fields are in data[1][1]
                    if len(data) > 1 and len(data[1]) > 1:
                        form_fields = data[1][1]
                        for field in form_fields:
                            if isinstance(field, list) and len(field) > 4:
                                field_id = field[0]
                                field_label = field[1]  # Label is in the second position
                                field_type = field[3]
                                
                                # Check if there are nested fields
                                if len(field) > 4 and isinstance(field[4], list):
                                    for nested_field in field[4]:
                                        if isinstance(nested_field, list) and len(nested_field) > 0:
                                            nested_id = nested_field[0]
                                            if isinstance(nested_id, int):
                                                base_id = f"entry.{nested_id}"
                                                form_mapping[base_id] = field_label
                                                if field_type == 10:  # Time input
                                                    form_mapping[f"{base_id}_hour"] = f"{field_label} (時)"
                                                    form_mapping[f"{base_id}_minute"] = f"{field_label} (分)"
                                                elif field_type == 9:  # Date input
                                                    form_mapping[f"{base_id}_year"] = f"{field_label} (年)"
                                                    form_mapping[f"{base_id}_month"] = f"{field_label} (月)"
                                                    form_mapping[f"{base_id}_day"] = f"{field_label} (日)"
                                else:
                                    base_id = f"entry.{field_id}"
                                    form_mapping[base_id] = field_label
                                    if field_type == 10:  # Time input
                                        form_mapping[f"{base_id}_hour"] = f"{field_label} (時)"
                                        form_mapping[f"{base_id}_minute"] = f"{field_label} (分)"
                                    elif field_type == 9:  # Date input
                                        form_mapping[f"{base_id}_year"] = f"{field_label} (年)"
                                        form_mapping[f"{base_id}_month"] = f"{field_label} (月)"
                                        form_mapping[f"{base_id}_day"] = f"{field_label} (日)"
                except (json.JSONDecodeError, IndexError) as e:
                    print(f"Error processing data: {str(e)}")
                    continue
    
    return form_mapping 
