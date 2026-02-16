#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

# 获取服务器IP地址
server_ip = socket.gethostbyname(socket.gethostname())
port = 8081
print(f"Starting server on {server_ip}:{port}")
print(f"Access via: http://{server_ip}:{port}")

# 创建HTTP服务器，监听所有接口
server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
server.serve_forever()
