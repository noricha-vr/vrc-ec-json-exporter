import json
from extract_form_ids import extract_form_ids_and_labels

def main():
    # Read the HTML file
    with open('outputs/google-form.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Extract form IDs and labels
    form_mapping = extract_form_ids_and_labels(html_content)

    # Convert to JSON and write to file
    with open('outputs/form_data.json', 'w', encoding='utf-8') as f:
        json.dump(form_mapping, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
