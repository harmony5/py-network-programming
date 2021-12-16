#!/usr/bin/python3
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

# Send file name
filename = input("filename: ")
client.sendall(filename.encode())

# Receive confirmation code
print("Receiving confirmation code...")
code = client.recv(1).decode()

if code == '1':
    print("[!] Error: server couldn't find file: {}".format(filename))
    client.shutdown(socket.SHUT_RDWR)  # Shutdown connection
    client.close()  # Close socket
    sys.exit(1)  # End program

print("Confirmed.")
# Send confirmation
client.send('0'.encode())

print("Opening file...")
file = open(filename, 'wb')

print("Receiving file...")
content = b''
data = client.recv(1024)  # Receive data
while data:
    content += data
    data = client.recv(1024)

# Write content to file
file.write(content)
file.close()

# Ends connection and close socket
client.shutdown(socket.SHUT_RDWR)
client.close()
sys.exit(0)
