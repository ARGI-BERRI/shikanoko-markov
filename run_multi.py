from concurrent.futures import ProcessPoolExecutor

from shikanoko.shikanoko import shikanoko_markov


if __name__ == "__main__":
    with ProcessPoolExecutor(16) as executor:
        results = [executor.submit(shikanoko_markov).result() for _ in range(10000)]

    print(sum(results) / 10000)
