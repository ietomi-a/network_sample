# coding:utf-8

from contextlib import closing
import socket
import sys
import time

# project module.
from connect_data import HOST, PORT, MOJI_CODE, BUFFER_SIZE

def send_message_by_socket( send_msg ):
    #send_msg = "hi2932"
    sock = socket.socket()
    with closing(sock):
        sock.connect( (HOST, PORT) )
        sock.send( send_msg.encode(MOJI_CODE) )
        result = sock.recv(BUFFER_SIZE)
    print( result.decode(MOJI_CODE) )
    return

def main():
    send_message_by_socket('hi first')
    send_message_by_socket('hi second!')
    send_message_by_socket('hi third!')        
    return
    
if __name__ == "__main__":
    main()
