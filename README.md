# blog-server
Dockerを用いて簡単に起動することのできる，ブログサーバーAPIである．

## 導入
1. リポジトリをクローンする
  ```shell
  git clone https://github.com/Shirashoji/blog-server
  ```
2. リポジトリに移動する
  ```shell
  cd blog-server
  ```
3.Docker Copmposeでコンテナを起動する[参考](https://docs.docker.jp/compose/reference/up.html)
  ```shell
  docker-compose up
  ```
  再ビルドする際は以下
  ```shell
  docker-compose up --build
  ```
4.あとは`http://localhost:80`でサーバーが起動するので，APIを叩くだけ．
