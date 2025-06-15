from math import sqrt


result = 0
for n in range(2, 10001):
    value = sqrt(n)
    x = int(value)
    if x**2 == n:
        continue
    a, b = x, n - x**2
    track = {(a, b): 0}
    current_index = 0
    while True:
        x = int((value + a) / b)
        a, b = b * x - a, (n - (a - b * x) ** 2) // b
        current_index += 1
        if first_index := track.get((a, b)):
            result += (current_index - first_index) % 2 == 1
            break
        track[(a, b)] = current_index
print(result)
