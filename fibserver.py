#!/usr/bin/python

from functools import lru_cache
import socket
import sys
import threading
import time

import fib
import socketutils

verbose = False;
if len(sys.argv) > 1 and (sys.argv[1] == '-v' or sys.argv[1] == '-V'):
    verbose = True;


@lru_cache(maxsize=256)
def cachedFib(n):
    return fib.fib(n);


class ServerThread (threading.Thread):
    def __init__(self, verbose):
        super(ServerThread, self).__init__();
        self.verbose = verbose;

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        server_address = ('localhost', 10000);
        if self.verbose:
            print('Starting up on {0} port {1}'.format(server_address[0], server_address[1]));
        sock.bind(server_address);
        sock.listen(1);
        while True:
            if self.verbose:
                print('Waiting for a connection');
            connection, client_address = sock.accept();
            try:
                if self.verbose:
                    print('Connection from ', client_address);
                while True:
                    if self.verbose:
                        print('\tAttempting recv_msg');
                    data = socketutils.recv_msg(connection);
                    if data:
                        n = int.from_bytes(data, byteorder='little');
                        if self.verbose:
                            print('\tn = ', n);
                        x = cachedFib(n);
                        if self.verbose:
                            print('\tx = ', x);
                        bit_length = x.bit_length();
                        byte_length = bit_length // 8 + 1;
                        response = x.to_bytes(byte_length, byteorder='little');
                        if self.verbose:
                            print('\tResponding...');
                        socketutils.send_msg(connection, response);
                    else:
                        if self.verbose:
                            print('\tNo more data from ', client_address);
                        break;
            finally:
                connection.close();


s = ServerThread(verbose);
s.daemon = True;
s.start();
try:
    while True:
        time.sleep(1);
except KeyboardInterrupt:
    sys.exit(0);