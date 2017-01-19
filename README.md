# FibonacciPy

Simple Python project for a client/server setup which calculates Fibonacci numbers. The server calculates the n^th Fibbonnaci by counting up, and caches the results for faster response in the future. 

## Installation

Just check out the git repository:

    $ git clone https://github.com/CoryOwens/FibonacciPy

## Running 

You can either run the `fibserver` in the background:

    $ ./fibserver.py &

Or in verbose mode (where debugging information will be output to standard output):

    $ ./fibserver.py -v

Once the server is running, you can run the client:

    $ ./fibcli.py {n}

Where `n` is any non-negative integer. 

## Testing

Start the server with the `runserver` script:

    $ ./runserver.sh

Then run the `test` script: 

    $ ./test.sh

If all tests pass, it will print `PASS`. If any fail, it will print the details of the failure, ass well as a harsh `FAIL`.

## Possible Errors

    Only one usage of each socket address (protocol/network address/port) is normally permitted

If you encounter the above error, you may already be running the `fibserver` in the background. Check your OS for running Python processes and kill as needed.
