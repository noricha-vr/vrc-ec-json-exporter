import json
from typing import Any

def export_json_file(data: Any, filepath: str) -> None:
    """
    データをJSONファイルとして出力する
    
    Args:
        data: 出力するデータ
        filepath (str): 出力先のファイルパス
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        raise Exception(f"JSONファイルの出力に失敗しました: {str(e)}") 
