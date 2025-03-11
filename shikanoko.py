import collections
import random

MAPPING = {
    "": ["し"],
    "し": ["か", "た"],
    "か": ["の"],
    "の": ["こ"],
    "こ": ["の", "の", "こ", "し"],
    "た": ["ん"],
    "ん": ["た", "."],
}


def next_token(token: str) -> str:
    return random.choice(MAPPING[token])


def get_markov_result() -> str:
    tokens: list[str] = []
    token = ""

    while token != ".":
        token = next_token(token)
        tokens.append(token)

    return "".join(tokens)


def main() -> None:
    results: list[str] = []
    result = ""

    while result != "しかのこのこのここしたんたん.":
        result = get_markov_result()
        results.append(result)
        print(result)

    for sentence, count in collections.Counter(results).most_common():
        print(count, sentence)


if __name__ == "__main__":
    main()
