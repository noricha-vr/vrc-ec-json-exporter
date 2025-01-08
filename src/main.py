import os
from get_google_form import get_google_form
from parse_output_html import extract_fb_public_load_data, extract_id_and_title
from save_html import save_html_to_file
from export_json_file import export_json_file

# 出力ディレクトリが存在しない場合は作成
os.makedirs('outputs', exist_ok=True)

# 設定
OUTPUT_FILE_PATH = 'outputs/google-form.html'
OUTPUT_JSON_FILE_PATH = 'outputs/event_data_param.json'
URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSevo0ax6ALIzllRCT7up-3KZkohD3VfG28rcOy8XMqDwRWevQ/formResponse'


def main():
    try:
        # GoogleフォームのHTMLを取得
        html = get_google_form(URL)

        # HTMLをファイルに保存
        save_html_to_file(html, OUTPUT_FILE_PATH)
        print(f'HTMLが {OUTPUT_FILE_PATH} に保存されました')

        # データを抽出
        data_list = extract_fb_public_load_data(html)
        if data_list is None:
            raise Exception("データの抽出に失敗しました")

        # IDとタイトルを抽出
        data_params = extract_id_and_title(data_list)

        # JSONファイルとして出力
        export_json_file(data_params, OUTPUT_JSON_FILE_PATH)
        print(f'データが {OUTPUT_JSON_FILE_PATH} に保存されました')

    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
