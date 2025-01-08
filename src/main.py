import os
from get_google_form import get_google_form
from parse_output_html import extract_fb_public_load_data, extract_id_and_title
from save_html import save_html_to_file
from export_json_file import export_json_file

# 出力ディレクトリのパスを修正
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 設定
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, 'google-form.html')
URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSevo0ax6ALIzllRCT7up-3KZkohD3VfG28rcOy8XMqDwRWevQ/formResponse'
OUTPUT_JSON_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'eventDataParam.json')

# ... 残りのコードは同じ ... 
