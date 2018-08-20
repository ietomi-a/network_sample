# coding: utf-8

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

host = 'localhost'
port = 8000

ctx = ssl.create_default_context( ssl.Purpose.CLIENT_AUTH )

# 下記コマンドで作成したもの.
#openssl x509 -in server.csr.pem -out server.crt -req -signkey private.key -days 365 -sha1
ctx.load_cert_chain('server.crt', keyfile='private.key')

# TLS 1.0, 1.1 を禁止する。
#ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

handler = SimpleHTTPRequestHandler
server = HTTPServer( (host, port), handler )
server.socket = ctx.wrap_socket( server.socket )

print("ok server start")
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()

print("server stop ok")

#https://localhost:8000/
