
def score(freq: dict, w: str) -> int:
    score = 0
    for letter in w:
        score += freq[letter]
    return score
