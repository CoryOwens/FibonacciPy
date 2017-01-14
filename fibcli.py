#!/usr/bin/python

import sys

import fib


if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] +" n");
    print("Prints the nth Fibonacci number.");
else:
    try:
        n = int(sys.argv[1]);
        x = fib.fib(n);
        print(x);
    except ValueError: 
        print("Invalid number: n must be an integer.");