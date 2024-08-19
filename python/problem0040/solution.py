from tqdm import tqdm


def run():
    print("Efficient")
    result = 1
    number, snumber = 1, "1"
    index = 0
    max_index = 10**6
    next_index = 1
    while next_index <= max_index:
        if index < next_index <= index + len(snumber):
            print(
                f"{next_index}th digit: {int(snumber[next_index - index - 1])}"
            )
            result *= int(snumber[next_index - index - 1])
            next_index *= 10
        index += len(snumber)
        number += 1
        snumber = str(number)

    print(f"Result: {result}")


if __name__ == "__main__":
    run()
