def run(value):
    for c in range(value // 3 + 1, value - 3):
        for b in range(1 + (value - c) // 2, min(c, value - c)):
            a = value - b - c
            if a**2 + b**2 == c**2:
                print(f"a: {a:,}, b: {b:,}, c: {c:,} -> abc = {a*b*c}")
                return
    print("Nothing found")


run(1000)
