import enum
import sys


class Colour(enum.Enum):
    green = 1  # present and in the correct location
    yellow = 2  # present but in another location
    grey = 3  # not present
    white = 4  # unused


def judge(guessWord, targetWord, wordLength) -> list:
    if len(guessWord) != wordLength or len(targetWord) != wordLength:
        sys.exit('Error: word length mismatch!')
    judgement = [None] * wordLength
    for i in range(wordLength):
        if targetWord[i] == guessWord[i]:
            judgement[i] = Colour.green
        elif guessWord[i] in targetWord:
            judgement[i] = Colour.yellow
        else:
            judgement[i] = Colour.grey
    return judgement
