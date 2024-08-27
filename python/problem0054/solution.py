from pathlib import Path
from collections import Counter, defaultdict
from functools import partial

vp = {
    **{str(v): v for v in range(2, 10)},
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def straight_rank(values):
    # 0 = not consecutive
    # 13 = consecutive, except "royal" T, J, Q, K, A
    # 14 = "royal consecutive" = T, J, Q, K, A
    return (len(set(values)) == 5) * (
        13 * (max(pos := list(map(vp.get, values))) - min(pos) == 4)
        + (min(pos) == 10)
    )


def flush_rank(suits):
    # 15 if all suits are the same otherwise 0
    return 15 * (len(suits) == 1)


def groups_rank(groups):
    # ranks the grouping of values.
    # basic rank: 6 if there is a pair, 12 for a triple and 18 for quatruple
    # additional 4 if there is a pair -> to destinguish triple and full house
    # additional 1 if there are two pairs -> to destinguish one and two pairs
    return (max(groups) - 1) * 6 + 4 * (2 in groups) + (len(groups[2]) == 2)


def get_ranking(cards):
    suits = {card[1] for card in cards}
    values = [card[0] for card in cards]

    # pairing maps card value to number of appearance
    pairings = Counter()
    for value in values:
        pairings[value] += 1
    # groups[2] contains the values of pairs
    groups = defaultdict(list)
    for value, size in pairings.items():
        groups[size].append(vp.get(value))

    game_rank = flush_rank(suits) + straight_rank(values) + groups_rank(groups)
    # largest groups value has to be compared first, see full house example
    rsort = partial(sorted, reverse=True)
    value_rank = [v for gk in rsort(groups) for v in rsort(groups[gk])]
    return [game_rank, *value_rank]


def run():
    wins = 0
    with open(
        Path(Path(__file__).parent, "poker.txt"), "r", encoding="utf-8"
    ) as fh:
        for i, line in enumerate(fh):
            cards = line.strip("\n").split(" ")
            wins += get_ranking(cards[:5]) > get_ranking(cards[5:])
    print(f"Player 1 wins {wins} times")


def test_ranking():
    rank_name = {
        0: "High card",
        10: "One Pair",
        11: "Two Pairs",
        12: "Three of a Kind",
        13: "Straight",
        14: "Royal",
        15: "Flush",
        16: "Full House",
        18: "Four of a Kind",
        28: "Straight Flush",
        29: "Royal Flush",
    }
    cases = {
        "High card": ["9H", "JS", "QH", "KH", "AH"],
        "One Pair": ["9H", "9S", "QH", "KH", "AH"],
        "Two Pairs": ["9H", "9S", "QH", "QS", "AH"],
        "Three of a Kind": ["9H", "9S", "9D", "KH", "AH"],
        "Straight": ["9H", "JS", "QH", "KH", "TH"],
        "Royal": ["TH", "JS", "QH", "KH", "AH"],
        "Flush": ["9H", "JH", "QH", "KH", "AH"],
        "Full House": ["9H", "9S", "9D", "KH", "KD"],
        "Four of a Kind": ["9H", "9S", "9D", "9C", "AH"],
        "Straight Flush": ["9H", "JH", "QH", "KH", "TH"],
        "Royal Flush": ["TH", "JH", "QH", "KH", "AH"],
    }
    for name, case in cases.items():
        print("=" * 50)
        print(f"Hand: {case} name: {name}")
        game_rank, *value_ranks = get_ranking(case)
        if name != (rname := rank_name[game_rank]):
            raise Exception(f"Expected hand: {name} vs ranked hand: {rname}")

    print("Ranking test successful\n")


def test_examples():
    examples = [
        ["5H 5C 6S 7S KD".split(" "), "2C 3S 8S 8D TD".split(" "), 0],
        ["5D 8C 9S JS AC".split(" "), "2C 5C 7D 8S QH".split(" "), 1],
        ["2D 9C AS AH AC".split(" "), "3D 6D 7D TD QD".split(" "), 0],
        ["4D 6S 9H QH QC".split(" "), "3D 6D 7H QD QS".split(" "), 1],
        ["2H 2D 4C 4D 4S".split(" "), "3C 3D 3S 9S 9D".split(" "), 1],
    ]
    for i, (p1, p2, result) in enumerate(examples, 1):
        if result and (r1 := get_ranking(p1)) < (r2 := get_ranking(p2)):
            raise Exception(
                f"Failed test {i}: p2 with {r2} should beat p1 with {r1}"
            )
        elif not result and (r1 := get_ranking(p1)) > (r2 := get_ranking(p2)):
            raise Exception(
                f"Failed test {i}: p1 with {r1} should beat p2 with {r2}"
            )
        print(f"Case {i} is correct: Win for player {2 - result}")

    print("Example tests successful\n")


if __name__ == "__main__":
    test_ranking()
    test_examples()
    run()
