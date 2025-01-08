def save_html_to_file(html: str, filepath: str) -> None:
    """
    HTMLをファイルに保存する
    
    Args:
        html (str): 保存するHTML文字列
        filepath (str): 保存先のファイルパス
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    except IOError as e:
        raise Exception(f"ファイルの保存に失敗しました: {str(e)}") 
