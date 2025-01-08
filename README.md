# VRC EC JSON Exporter

GoogleフォームからデータをスクレイピングしてJSONファイルとして出力するツールです。

## 必要要件

- Python 3.12以上
- [uv](https://github.com/astral-sh/uv) (Pythonパッケージマネージャー)

## セットアップ

```bash
# 依存パッケージのインストール
uv pip install -e .
```

## 使用方法

```bash
# スクリプトの実行
python -m src.main
```

実行すると以下のファイルが生成されます：

- `outputs/google-form.html`: 取得したGoogleフォームのHTML
- `eventDataParam.json`: 抽出したID、タイトルのデータ

## 出力形式

`eventDataParam.json`は以下の形式で出力されます：

```json
[
  {
    "id": 123456789,
    "title": "質問のタイトル"
  },
  ...
]
```

## 開発環境

- Python 3.12
- requests: HTTPリクエスト用ライブラリ
- types-requests: requestsの型定義
