#!/usr/bin/python3
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

server = socket.socket()
server.bind(('', port))

print("Waiting for connection...")
server.listen(1)

client, addr = server.accept()
print("Connected to: {}:{}".format(*addr))

# Receive name of file
print("Receiving filename...")
filename = client.recv(100).decode()

print("Filename:", filename)

# Try to open file
try:
    print("Opening file: {}...".format(filename))
    file = open(filename, 'rb')
    print('opened')
except FileNotFoundError:
    print("[!] Error: couldn't find file: {}".format(filename))
    client.sendall('1'.encode())  # Send error code
    client.shutdown(socket.SHUT_RDWR)  # Shutdown connection
    client.close()  # Close socket
    sys.exit(1)  # End program

print('here')
# Send file
client.sendall('0'.encode())
print("Confirmation:", client.recv(1))
print("Sending file...")
content = file.read(1024)
while content:
    client.send(content)
    content = file.read(1024)

print("Done.")
file.close()
client.shutdown(socket.SHUT_RDWR)
client.close()
sys.exit(0)
