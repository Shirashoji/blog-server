# 公式のPythonベースイメージ
FROM python:3.10

# パッケージのインストールをする場所
WORKDIR /code

# requirements.txtをコンテナにコピー
COPY ./requirements.txt /code/requirements.txt

# pipでrequirements.txtに書かれたパッケージをインストール
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# アプリケーションのコードをコンテナにコピー
COPY app /code/app

# アプリケーションのコードをコンテナ内で実行する場所
WORKDIR /code/app

# コンテナ起動時にデフォルトで実行するコマンド，uvicornでFastAPIを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]