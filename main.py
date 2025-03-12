import collections

from shikanoko.shikanoko import get_markov_result


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
