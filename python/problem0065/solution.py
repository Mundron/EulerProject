sequence = [2, *(x for k in range(1, 34) for x in (1, 2 * k, 1))]

a, b = 1, sequence[-1]
for x in reversed(sequence[:-1]):
    a, b = x * a + b, a
print(sum(map(int, str(a))))
