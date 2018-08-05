server を起動させる
  python server.py start

client を動作させる.
  python client.py

server を停止させる
  python server.py stop

注意: server 停止直後に server を再び起動させようとすると、
     port が確保できないで起動しないことがある。この場合、10秒くらい時間を置いてから
     起動させること.
