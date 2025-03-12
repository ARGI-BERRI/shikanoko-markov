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
