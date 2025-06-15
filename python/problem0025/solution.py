lower_limit, index, a, b = 10**999, 1, 0, 1
while b < lower_limit:
    index, a, b = index + 1, b, a + b

print(f"{index}:")
print(f"Number: {b}")
print(f"Size of number: {len(str(b)):,}")
