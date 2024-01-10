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
3.Docker Copmposeでビルドする．[参考](https://docs.docker.jp/compose/reference/build.html)
  ```shell
  docker-compose build
  ```
4.コンテナを起動する[参考](https://docs.docker.jp/compose/reference/up.html)
  ```shell
  docker-compose up
  ```
5.あとは`http://localhost:80`でサーバーが起動するので，APIを叩くだけ．
