#!/usr/bin/python3

import socket_file_transfer
import socket
import sys

args = sys.argv[1:]
if not args:
    print("usage: file_transfer_client 'host' 'port'")
    sys.exit(1)

try:
    host = args[0]
    port = int(args[1])
except IndexError:
    print("usage: file_transfer_client 'host' 'port'")
    sys.exit(1)
except ValueError:
    print("[!] Error: 'port' must be a number.")
    sys.exit(1)

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
print("Connecting to {}:{}...".format(host, port))
client.connect((host, port))
print("Connected to {}:{}".format(host, port))

# Send file name
filename = input("filename: ")
client.sendall(filename.encode())
# Receive file
print("Receiving file...")
socket_file_transfer.recv_file(client, filename)

print("File received.")
# Ends connection and close socket
client.shutdown(socket.SHUT_RDWR)
client.close()
sys.exit(0)
