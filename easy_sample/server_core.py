# coding:utf-8

from contextlib import closing
from datetime import datetime
import os
import signal
import socket
import sys
import time
import traceback

# project module.
from connect_data import HOST, PORT, MOJI_CODE, BUFFER_SIZE

LOG_PATH = "server_log.txt"
PID_DATA_PATH = "server_pid.txt"
LISTEN_NUM = 5


def act_for_access( client_sock ):
    recv_msg_tmp = client_sock.recv(BUFFER_SIZE)
    recv_msg = recv_msg_tmp.decode(MOJI_CODE)
    date_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    with open( LOG_PATH, "a" ) as g:        
        g.write( '%s : Received -> %s\n' % (date_str, recv_msg) );
        g.flush()
    send_msg = "accept: %s ok" % recv_msg
    client_sock.send( send_msg.encode(MOJI_CODE) )
    return

def is_running(pid):        
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True

def server_stop():
    if not os.path.exists(PID_DATA_PATH):
        print("server is not started")
        return
    with open( PID_DATA_PATH, "r") as f:
        pid = int(f.readline())

    os.kill( pid, signal.SIGTERM ) 
    while is_running(pid):
        time.sleep(1)
    os.remove( PID_DATA_PATH )
    return


def server_start():
    if os.path.exists( LOG_PATH ):
        os.remove( LOG_PATH )
    with open( PID_DATA_PATH, "w") as g:
        g.write( "%d\n" % os.getpid() )
    # socket.AF_INET -> IP での通信を意味する。
    # socket.SOCK_STREAM -> TCP での通信を意味する。
    # (ちなみに UDP の場合は socket.SOCK_DGRAM を指定。
    server_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server_sock.bind( (HOST,PORT) ) #IPとPORTを指定してバインドします
    server_sock.listen( LISTEN_NUM ) # #接続の待ち受けをします（キューの最大数を指定）
    with closing(server_sock):    
        while True:
            client_sock, client_address = server_sock.accept() # 接続まち.
            with closing(client_sock):
                act_for_access( client_sock )
    return

if __name__ == "__main__":
    server_start()
