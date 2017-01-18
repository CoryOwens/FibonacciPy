#!/usr/bin/python

import socket
import sys
import struct


if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] +" n");
    print("Prints the nth Fibonacci number.");
    sys.exit(-1);

try:
    n = int(sys.argv[1]);
except ValueError: 
    print("Invalid number: n must be an integer.");
    sys.exit(-1);

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server_address = ('localhost', 10000);
sock.connect(server_address);
try:
    request = n.to_bytes(16, byteorder='big');
    sock.sendall(request);
    amount_received = 0;
    amount_expected = 1024;
    while amount_received < amount_expected:
        data = sock.recv(1024);
        amount_received += len(data);
        x = int.from_bytes(data, byteorder='big');
        print(x);
finally:
    sock.close();

