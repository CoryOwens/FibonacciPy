#!/usr/bin/python

import socket
import sys
import threading
import time

import fib

class ServerThread (threading.Thread):
    def run (self): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        server_address = ('localhost', 10000);
        print('Starting up on %s port %s' % server_address);
        sock.bind(server_address);
        sock.listen(1);


        while True:
            print('Waiting for a connection');
            connection, client_address = sock.accept();
            try:
                print('Connection from ', client_address);
                while True:
                    data = connection.recv(16);
                    if data:
                        n = int.from_bytes(data, byteorder='big');
                        print('Received "%i"' % n);
                        x = fib.fib(n);
                        print('Sending response back to client: %i' % x);
                        connection.sendall(x.to_bytes(1024, byteorder='big'));
                    else:
                        print('No more data from ', client_address);
                        break
                    
            finally:
                connection.close()

s = ServerThread();
s.daemon = True;
s.start();
try:
    while True:
        time.sleep(1);
except KeyboardInterrupt: 
    sys.exit(0);