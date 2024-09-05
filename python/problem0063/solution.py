from itertools import count


def run():
    result = 0
    for power in count(1, 1):
        for base in range(1, 10):
            number = str(base**power)
            if len(number) > power:
                break
            elif len(number) == power:
                print(f"{base} ** {power} = {number}")
                result += 1
        if len(number) < power:
            break
    print(result)


if __name__ == "__main__":
    run()
