#!/usr/bin/python3
import socket
import sys

if len(sys.argv) < 2:
    print('usage: tcp_server port')
    sys.exit(1)

GREEN = '\033[38;5;82m'
RED = '\033[38;5;'
print(GREEN)

# Banner
print("================")
print("|| TCP Server ||")
print("================")


port = int(sys.argv[1])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(1)

client, addr = server.accept()

print("Received connection from {}:\033[1m\033[7m{}\033[27m\033[21m".format(addr[0], addr[1]))

# Server loop:
while 1:

    data = client.recv(1024)
    if not data:
        client.shutdown(socket.SHUT_RDWR)
        break  # if there's no more data to receive.

    print("Received Data:\n", data)
    client.send("ACK!".encode())

client.close()
