import re
import json
from typing import Any, List, Dict

def extract_fb_public_load_data(html: str) -> Any:
    """
    HTMLからFB_PUBLIC_LOAD_DATA_の内容を抽出する
    
    Args:
        html (str): 取得したHTML文字列
    
    Returns:
        Any: パースしたデータ
    """
    regex = r"var FB_PUBLIC_LOAD_DATA_ = (\[.*?\]);"
    match = re.search(regex, html, re.DOTALL)
    
    if match and match.group(1):
        data_string = match.group(1)
        try:
            return json.loads(data_string)
        except json.JSONDecodeError as e:
            print(f'JSONのパースに失敗しました: {e}')
            return None
    else:
        print('FB_PUBLIC_LOAD_DATA_が見つかりませんでした。')
        return None

def extract_id_and_title(data: Any) -> List[Dict[str, Any]]:
    """
    FB_PUBLIC_LOAD_DATA_のデータから[ID, "タイトル"]を抽出する
    
    Args:
        data: FB_PUBLIC_LOAD_DATA_のデータ
    
    Returns:
        List[Dict[str, Any]]: {id: number, title: string}の配列
    """
    results = []
    
    def traverse(node: Any) -> None:
        if isinstance(node, list):
            if (len(node) >= 2 and 
                isinstance(node[0], (int, float)) and 
                isinstance(node[1], str) and 
                node[1] is not None):
                results.append({"id": node[0], "title": node[1]})
            
            for child in node:
                traverse(child)
        elif isinstance(node, dict):
            for value in node.values():
                traverse(value)
    
    traverse(data)
    return results 
