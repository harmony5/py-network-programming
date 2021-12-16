#!/usr/bin/python3

# TCPServer processes requests synchronously (each request must be completed before the next request can be started).
# ForkingMixIn and ThreadingMixIn support multithreading, hence processing requests asynchronously.

import socket
import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).decode()
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data).encode()
        self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message.encode())
        response = sock.recv(1024).decode()
        print("Received: {}".format(response))
    finally:
        sock.close()


if __name__ == '__main__':
    def main():
        HOST, PORT = 'localhost', 0
        server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
        ip, port = server.server_address

        # Start new thread with server
        # This server thread will start a new thread for each request

        server_thread = threading.Thread(target=server.serve_forever)

        # Exit the server thread when the main finishes
        server_thread.daemon = True
        server_thread.start()
        print("Server running in thread: {}".format(server_thread.name))

        client(ip, port, "Hello One.")
        client(ip, port, "Hello Two.")
        client(ip, port, "Hello Three.")

        server.shutdown()

    main()
