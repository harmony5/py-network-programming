#! /usr/bin/python3

"""
Port: is a place where information goes into and out of a computer.

Port scanner: application designed to probe a server or host for open ports.

Port scan or portscan: process that sends client requests to a range of server port addresses on a host, with the goal of finding an active port.

To portsweep: to scan multiple hosts for a specific listening port. The latter is typically used to search for a specific service.
"""

import socket
import sys


def is_port_open(host, port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        connection.connect((host, port))
        connection.close()
        return True

    except Exception:
        return False


def port_roulette(host, start, end, step=1):
    open_ports = set()

    for port in range(start, end + 1, step):
        if is_port_open(host, port):
            open_ports.add(port)

    return open_ports


if __name__ == '__main__':
    import time

    def main():
        args = sys.argv[1:]
        if not args:
            print('usage: p_scan host start end [step]')
            sys.exit(1)

        host = args[0]
        host = socket.gethostbyname(host)
        step = 1
        try:
            start = int(args[1])
            end = int(args[2])
            del args[:3]
            if args:
                step = int(args[0])
        except ValueError:
            print("[!] Error: 'start' 'stop' and 'step' must be integers.")
            sys.exit(1)
        start_time = time.time()
        open_ports = port_roulette(host, start, end, step)
        if len(open_ports) != 0:
            print("Open ports in host '{}' ({}):".format(host, len(open_ports)))
            for pr in open_ports:
                print("  port {}".format(pr))
        else:
            print("Host '{}' has no open ports in the given range ({}, {}, {}).".format(host, start, end, step))
        total = time.time() - start_time
        print("Total time taken:", total)
    main()
