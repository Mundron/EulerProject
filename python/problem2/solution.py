def fib(limit):
    x, y = 0, 1
    while x + y < limit:
        x, y = y, x + y
        yield y


print(sum(x for x in fib(4 * 10**6) if not x % 2))
