import math


def get_ascii_dict(start: int, end: int) -> dict:
    """start is included, end is excluded"""
    ascii_dict = {}
    for current in range(start, end):
        ascii_dict[chr(current)] = 0
    return ascii_dict


def analyze_frequency(text_file: str, ascii_freq: dict) -> dict:
    ascii_signs = ascii_freq.keys()
    with open(text_file, "r") as file:
        current = file.read(1).lower()
        while current != "":
            if current in ascii_signs:
                ascii_freq[current] += 1
            current = file.read(1).lower()
    return ascii_freq


def get_cardinality(ascii_freq: dict) -> int:
    cardinality = 0
    for key in ascii_freq.keys():
        cardinality += ascii_freq[key]
    return cardinality


def get_distribution(ascii_freq: dict) -> dict:
    cardinality = get_cardinality(ascii_freq)
    ascii_dist = {}
    for key in ascii_freq:
        ascii_dist[key] = ascii_freq[key] / cardinality
    return ascii_dist


def calculate_entropy(distribution: dict, base=2) -> float:
    entropy = 0
    for probability in distribution.values():
        entropy -= probability * math.log(probability, base)
    return entropy


if __name__ == "__main__":
    alphabet_freq = analyze_frequency("ulysses.txt", get_ascii_dict(97, 123))
    cardinality = get_cardinality(alphabet_freq)
    alphabet_dist = get_distribution(alphabet_freq)
    entropy = calculate_entropy(alphabet_dist)

    # Now we have calculated the entropy of Ulysses by James Joyce, although we
    # just looked at the letters and disregarded higher and lowercase
    # If we were to encode this data (just lowercase letters) without
    # compression we would need cardinality*log_2(number_of_letters) BITS,
    # using a compression algorithm with perfect compression rate on the other
    # hand we would just need cardinality*entropy BITS

    print(
        "This is the approximated distribution of letters in the english language by using Ulysses:")
    print(alphabet_dist)
    print("The entropy is", entropy)
    print("A compression-algorithm with perfect compression rate would need",
          cardinality * entropy, "BITS")
    print("This is",cardinality * entropy/(8*1024), "Kilo-Byte")
