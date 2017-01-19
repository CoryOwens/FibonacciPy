#!/usr/bin/python

import socket
import sys
import struct

import socketutils


if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0] +' n');
    print('Prints the nth Fibonacci number.');
    sys.exit(-1);

try:
    n = int(sys.argv[1]);
except ValueError:
    print('Invalid number: n must be a non-negative integer.');
    sys.exit(-1);
if n < 0:
    print('Invalid number: n must be a non-negative integer.');
    sys.exit(-1);

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server_address = ('localhost', 10000);
sock.connect(server_address);
try:
    message = n.to_bytes((n.bit_length() // 8) + 1, byteorder='little');
    socketutils.send_msg(sock, message);
    data = socketutils.recv_msg(sock);
    x = int.from_bytes(data, byteorder='little');
    print(x);
finally:
    sock.close();

