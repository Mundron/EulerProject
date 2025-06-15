def is_palindrom(value):
    value_string = str(value)
    if not (half := len(value_string) // 2):
        return True
    start, end = value_string[:half], value_string[-half:]
    return start == end[::-1]


result = 0
for x in range(100, 1000):
    for y in range(100, x):
        candidate = x * y
        if is_palindrom(candidate) and candidate > result:
            result = candidate

print(result)
