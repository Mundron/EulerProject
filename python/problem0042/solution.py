from pathlib import Path

words_path = Path(Path(__file__).parent, "words.txt")

max_triangle = 1
max_index = 1
known_triangles = {1}


def is_triangle(value):
    global max_triangle
    global max_index
    global known_triangles
    while value > max_triangle:
        max_index += 1
        max_triangle = max_index * (max_index + 1) // 2
        known_triangles.add(max_triangle)

    return value in known_triangles


def get_value(txt):
    return sum(ord(c) - 64 for c in txt)


def run():
    wcnt, tcnt = 0, 0
    with open(words_path, "r", encoding="utf-8") as fh:
        for line in fh:
            for word in line.split(","):
                wcnt += 1
                if is_triangle(get_value(word.strip('"'))):
                    tcnt += 1
    print(f"Found {tcnt} triangle words out of {wcnt} words")


if __name__ == "__main__":
    run()
