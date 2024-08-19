from itertools import permutations

digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
position = 10**6

for pos, com in enumerate(permutations(digits, len(digits)), 1):
    if pos == position:
        break

print("".join(map(str, com)))
