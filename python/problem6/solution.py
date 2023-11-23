def run(limit):
    print(sum(range(limit + 1)) ** 2 - sum(x**2 for x in range(limit + 1)))


run(100)
