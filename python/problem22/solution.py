def alpha_ord(character):
    return ord(character) - 64


with open("0022_names.txt") as filehandle:
    for names in filehandle:
        pass


result = 0

for position, name in enumerate(sorted(names.split(",")), 1):
    result += sum(map(alpha_ord, name.replace('"', ""))) * position

print(f"Sum of name scores: {result}")
