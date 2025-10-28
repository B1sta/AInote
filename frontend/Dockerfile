# ベースイメージ
FROM node:18-alpine

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をインストール
COPY package.json .
COPY package-lock.json .
RUN npm install

# ソースコードをコピー
COPY . .