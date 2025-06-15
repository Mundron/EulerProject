from eputils.utils import Triagonal, Pentagonal, Hexagonal


def run():
    tri, penta, hexa = Triagonal(), Pentagonal(), Hexagonal()
    for number in hexa:
        if number <= 40755:
            continue
        if number in tri and number in penta:
            print(f"Found the next triple value {number}")
            break


if __name__ == "__main__":
    run()
