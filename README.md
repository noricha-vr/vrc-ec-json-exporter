# VRC EC JSON Exporter

GoogleフォームからデータをスクレイピングしてJSONファイルとして出力するツールです。

## 必要要件

- Python 3.12以上
- [uv](https://github.com/astral-sh/uv) (Pythonパッケージマネージャー)

## インストール

```bash
# リポジトリのクローン
git clone git@github.com:noricha-vr/vrc-ec-json-exporter.git
cd vrc-ec-json-exporter

# 依存パッケージのインストール
uv venv
source .venv/bin/activate  # Unix/macOS の場合
# または .venv\Scripts\activate  # Windows の場合
uv pip install -e .
```

## 使用方法

```bash
# 仮想環境のアクティベーション（まだアクティベートしていない場合）
source .venv/bin/activate  # Unix/macOS の場合
# または .venv\Scripts\activate  # Windows の場合

# スクリプトの実行
cd src
python main.py
```

実行すると以下のファイルが生成されます：
- `outputs/google-form.html`: 取得したGoogleフォームのHTML
- `outputs/event_data_param.json`: 抽出したID、タイトルのデータ

## 出力形式

`event_data_param.json`は以下の形式で出力されます：

```json
[
  {
    "id": 123456789,
    "title": "質問のタイトル"
  }
]
```

## 開発環境のセットアップ

1. Python 3.12のインストール
```bash
# asdfを使用する場合
asdf install python 3.12
asdf local python 3.12

# pyenvを使用する場合
pyenv install 3.12
pyenv local 3.12
```

2. uvのインストール
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 開発環境

- Python 3.12
- requests: HTTPリクエスト用ライブラリ
- types-requests: requestsの型定義

## ライセンス

MIT License
