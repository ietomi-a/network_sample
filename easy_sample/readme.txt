概要
　クライアントはサーバーにメッセージを送信する。
  サーバーは受け取ったメッセージを server_log.txt に書き込み、
  メッセージを受け取った旨をクライアントに返す。

使い方
  server を起動させる
    python server.py start

  client を動作させる.
    python client.py

  server を停止させる
    python server.py stop

注意 1: python3 での実行を想定しているため packet の中身をバイナリに変換している。
       python2 での場合、このような操作は必要ないと思われるが試していない。      

注意2 : server 停止直後に server を再び起動させようとすると、
       同じ port が確保できないため起動しないことがある。
       この場合、10秒くらい時間を置いてから起動させること.
