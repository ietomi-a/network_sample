# coding:utf-8

from contextlib import closing
from datetime import datetime
import os
import socket
import sys
import time
import traceback

# project module.
from connect_data import HOST, PORT, MOJI_CODE, BUFFER_SIZE
from server_core import server_stop


def check_server_socket_bind():
    server_sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    try:
        server_sock.bind( (HOST,PORT) ) #IPとPORTを指定してバインド.
    except:
        traceback.print_exc()
        print("connect_data.PORT may be already used. you need to change connect_data.PORT.")
        exit(1)


def main( argv ):
    if len(argv) != 2:
        print( "len(sys.argv) must be is 2, but sys.argv =", argv )
    elif argv[1] == "start":
        check_server_socket_bind()
        os.system("python server_core.py &")
    elif argv[1] == "stop":
        server_stop()
    else:
        print("usage: python server.py {start|stop}, but sys.argv[1] is neihter start nor stop, sys.argv[1] = ", sys.argv[1] )
              
    return


if __name__ == "__main__":
    main( sys.argv )
