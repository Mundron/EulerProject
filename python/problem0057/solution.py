def run():
    x, y, result = 3, 2, 0
    for _ in range(1000):
        result += len(str(x)) > len(str(y))
        x, y = x + 2 * y, x + y

    print(result)


if __name__ == "__main__":
    run()
