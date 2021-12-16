#!/usr/bin/python3

import socketserver
import sys


class TCPSocketHandler(socketserver.BaseRequestHandler):
    """
    RequestHandler for tcp servers.
    It is instantiated once per connection to the server.
    """

    def handle(self):
        # self.request is the tcp socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.request.sendall(self.data.upper())  # send back data received uppercased


if __name__ == '__main__':
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

    # Instantiate the server, and bind to host, port
    server = socketserver.TCPServer((host, port), TCPSocketHandler)

    # Activate server
    # Ctrl-C to exit
    server.serve_forever()

# TCPServer processes requests synchronously (each request must be completed before the next request can be started).
# ForkingMixIn and ThreadingMixIn support multithreading, hence processing requests asynchronously.
