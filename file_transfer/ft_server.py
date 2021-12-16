#!/usr/bin/python3

import socket_file_transfer
import socket
import sys

args = sys.argv[1:]
if not args:
    print("usage: file_transfer_server 'port'")
    sys.exit(1)

try:
    port = int(args[0])
except ValueError:
    print("[!] Error: 'port' must be a number")
    sys.exit(1)

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))  # bind to port

# Wait for connection
print("Waiting for connection...")
server.listen(5)

while 1:
    # Receive connection
    client, addr = server.accept()
    print("Connected to: {}:{}".format(*addr))

    # Receive file name
    print("Receiving filename...")
    filename = client.recv(100).decode()
    print("Filename:", filename)

    # Send file
    print("Sending file...")
    socket_file_transfer.send_file(client, filename)

    print("File sent.")
    print("Done.")

    client.shutdown(socket.SHUT_RDWR)
    client.close()

sys.exit(0)
