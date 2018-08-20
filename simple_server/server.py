# coding:utf-8
import http.server
import socketserver

HOST = "ietomi.dev"
PORT = 8091
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer( (HOST, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


