import random


def next_token(token: str) -> str:
    match token:
        case "し":
            return random.choice(["か", "た"])
        case "か":
            return "の"
        case "の":
            return "こ"
        case "こ":
            return random.choice(["の", "の", "こ", "し"])
        case "た":
            return "ん"
        case "ん":
            return random.choice(["た", "."])
        case ".":
            return random.choice([".", "し"])

    raise ValueError(f"not supported token: {token}")


def join(chain: list[str]):
    return "".join(chain)


def shikanoko_markov():
    i = 0

    while True:
        i += 1
        current_token = "し"
        chain = ["し"]

        while True:
            current_token = next_token(current_token)
            chain.append(current_token)

            if current_token == ".":
                break

        sentence = join(chain)

        print(sentence)

        if sentence == "しかのこのこのここしたんたん.":
            return i
