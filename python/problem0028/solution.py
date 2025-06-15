def run(size):
    result = 1
    last_corner = 1
    for jump in range(2, size + 1, 2):
        result += 4 * last_corner + 10 * jump
        last_corner += 4 * jump

    print(f"Sum of {size}x{size} spiral is {result}")


if __name__ == "__main__":
    run(1001)
