import requests
from typing import Optional
from urllib.parse import urlparse

def get_google_form(url: str) -> str:
    """
    GoogleフォームのHTMLを取得する
    
    Args:
        url (str): GoogleフォームのURL
    
    Returns:
        str: 取得したHTML
    
    Raises:
        requests.RequestException: リクエストに失敗した場合
    """
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise Exception(f"リクエストが失敗しました: {str(e)}") 
