# -*- coding: utf-8 -*-
import socket
import json

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))
send_str = u'Привет из Москвы'
send_data = json.dumps(dict(msg=send_str))
print('SEND DATA: ', send_data)
client_sock.sendall(send_data)
data = client_sock.recv(1024)
client_sock.close()
print('Received', repr(data))