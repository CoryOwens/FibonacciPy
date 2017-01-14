

def fib(n):
    if n is None or n < 0:
        return None;
    if n == 0:
        return 0;
    if n == 1 or n == 2:
        return 1;
    cur = 0;
    a = 1;
    b = 1;
    count = 2;
    while (count < n):
        cur = a + b;
        a = b;
        b = cur;
        count += 1;
    return cur;

