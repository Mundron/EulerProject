def get_chain_length(number):
    result = 1
    while number > 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number //= 2
        result += 1
    return result


def run(limit):
    best_num, best_len = 1, 1
    for number in range(2, limit):
        if (chain_len := get_chain_length(number)) > best_len:
            best_num, best_len = number, chain_len
    print(f"Best number {best_num:,} has a chain length of {best_len:,}")


if __name__ == "__main__":
    run(10**6)
