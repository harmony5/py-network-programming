#!/usr/bin/python3
import socket
import sys


if len(sys.argv) < 3:
    print('usage: tcp_client hostname port')
    sys.exit(1)

host = sys.argv[1]

try:
    port = int(sys.argv[2])
except ValueError:
    print("[!] Error: 'port' must be a number.")
    sys.exit(1)


# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect the client
client.connect((host, port))

MSG = input("MSG: ")

# Send some data
client.sendall(MSG.encode())  # use sendall to send all data, send can fail and just send some not all.

# Recieve data until there is no more to receive.
while 1:
    data = client.recv(1024)
    if not data:
        client.shutdown(socket.SHUT_RDWR)
        break
    print(data)


print(data)
client.close()
sys.exit(0)
