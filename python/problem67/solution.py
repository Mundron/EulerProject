def load_triangle():
    with open("0067_triangle.txt") as filehandle:
        return [list(map(int, line.split(" "))) for line in filehandle]


def run():
    triangle = load_triangle()
    line = triangle[0]

    for row in range(1, len(triangle)):
        new_line = triangle[row]
        for column in range(len(new_line)):
            if column == 0:
                new_line[0] += line[0]
            elif column == len(new_line) - 1:
                new_line[-1] += line[-1]
            else:
                new_line[column] += max(line[column - 1 : column + 1])
        line = new_line

    print(max(line))


if __name__ == "__main__":
    run()
