import shutil


def send_file(socket, filename):
    with open(filename, 'rb') as file:
        out_socket = socket.makefile('wb')
        shutil.copyfileobj(file, out_socket)


def recv_file(socket, filename):
    with open(filename, 'wb') as file:
        in_socket = socket.makefile('rb')
        shutil.copyfileobj(in_socket, file)
