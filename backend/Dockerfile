# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . /app/