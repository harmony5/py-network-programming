#!/usr/bin/python3
import socket
import sys

if len(sys.argv) < 2:
    print("usage: echo_server 'port'")
    sys.exit(1)

port = 0
try:
    port = int(sys.argv[1])
except ValueError:
    print("[!] Error: 'port' must be an integer.")
    sys.exit(1)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create tcp socket
server.bind(('', port))  # bind to port
server.listen(1)  # wait for connection

client, addr = server.accept()  # accepts connection
print('Connection from: {}:{}'.format(*addr))

data = client.recv(4096)
while len(data) > 0:
    client.sendall(data)
    data = client.recv(4096)
    if not data:
        break


client.close()
