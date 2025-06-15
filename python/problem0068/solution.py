from itertools import chain


def get_gons(part_gon, numbers):
    if len(numbers) == 1:
        n = numbers.pop()
        last_line = [n, part_gon[-1][-1], part_gon[0][1]]
        if sum(part_gon[-1]) == sum(last_line):
            yield part_gon + [last_line]
    else:  # numbers contains at least 2 elements
        total, ref = sum(part_gon[-1]), part_gon[-1][-1]
        seen = set()
        for n in numbers:
            if n in seen:
                continue
            m = total - n - ref
            if m < 1 or m == n or m not in numbers:
                continue
            yield from get_gons(part_gon + [[n, ref, m]], numbers - {n, m})
            yield from get_gons(part_gon + [[m, ref, n]], numbers - {n, m})
            seen.add(m)


def stringify(gon):
    if not gon:
        return ""

    i = 0
    minval = gon[0]
    for j, g in enumerate(gon[1:], 1):
        if g < minval:
            i = j
            minval = g

    return "".join("".join(map(str, g)) for g in gon[i:] + gon[:i])


def run():
    res = ""
    numbers = set(range(1, 10))
    for x in range(9, 1, -1):
        for y in range(x - 1, 0, -1):
            sub = numbers - {x, y}
            gons = chain(
                get_gons([[10, x, y]], sub), get_gons([[10, y, x]], sub)
            )
            res = max(max(map(stringify, gons), default=""), res)
    print(res)


if __name__ == "__main__":
    run()
