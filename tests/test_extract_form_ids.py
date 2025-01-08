import pytest
from src.extract_form_ids import extract_form_ids

def test_extract_form_ids():
    # Expected form IDs based on the provided form_data
    expected_ids = {
        'entry.426573786',  # イベント名
        'entry.1010494053_hour',  # 開始時刻（時）
        'entry.1010494053_minute',  # 開始時刻（分）
        'entry.203043324_hour',  # 終了時刻（時）
        'entry.203043324_minute',  # 終了時刻（分）
        'entry.450203369_year',  # 日付（年）
        'entry.450203369_month',  # 日付（月）
        'entry.450203369_day',  # 日付（日）
        'entry.1261006949',  # Android対応可否
        'entry.2064647146',  # 参加条件
        'entry.1540217995',  # イベント主催者
        'entry.1285455202',  # 参加方法
        'entry.586354013',  # 備考
        'entry.1607289186',  # 海外ユーザー向け告知
        'entry.701384676',  # イベント内容
    }

    # Read the HTML file
    with open('outputs/google-form.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Extract actual form IDs
    actual_ids = set(extract_form_ids(html_content))

    # Check if all expected IDs are present in the actual IDs
    missing_ids = expected_ids - actual_ids
    assert not missing_ids, f"Missing expected form IDs: {missing_ids}"

    # Print all found IDs for reference
    print("\nAll found form IDs:")
    for form_id in sorted(actual_ids):
        print(f"- {form_id}")

    # Print missing IDs if any
    if missing_ids:
        print("\nMissing IDs:")
        for form_id in sorted(missing_ids):
            print(f"- {form_id}")

    # Print unexpected IDs if any
    unexpected_ids = actual_ids - expected_ids
    if unexpected_ids:
        print("\nUnexpected IDs:")
        for form_id in sorted(unexpected_ids):
            print(f"- {form_id}")

    # Additional assertions
    assert len(actual_ids) > 0, "No form IDs were found"
    assert 'entry.426573786' in actual_ids, "Event name ID not found" 
