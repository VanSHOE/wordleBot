from string import ascii_lowercase
from scorer import score
from judge import judge, Colour
from typing import Tuple


# returns the correct guess and the number of guesses made
def guesser(wordLength: int, targetWord: str, possibleWords: dict, printGuess=False) -> Tuple[str, int]:
    freq = {x: 0 for x in ascii_lowercase}

    with open("data/dictionary.txt", 'r') as f:
        # find the frequencies of each letter
        for word in f:
            if len(word) == wordLength:
                for letter in word.strip():
                    freq[letter] += 1
        f.seek(0)

        # initialise the scores
        for word in f:
            w = word.strip()
            if len(w) == wordLength:
                possibleWords[w] = score(freq, w)

        # print(f'targetWord = {targetWord}')

        guessCount = 0  # number of guesses needed to guess the word
        while True:
            # return key with maximum value in dictionary
            guessWord = max(possibleWords, key=possibleWords.get)
            guessCount += 1

            if printGuess:
                print(f"Guess number {guessCount}: {guessWord}")

            judgement = judge(guessWord, targetWord, wordLength)
            # print(f'Judgement: {[x.name for x in judgement]}')

            wordsToDelete = set()

            if judgement == [Colour.green] * wordLength:
                break
            else:
                wordsToDelete.add(guessWord)

            # greyLetters = set()
            for i, colour in enumerate(judgement):
                if colour == Colour.green:
                    for word in possibleWords.keys():
                        if word[i] != guessWord[i]:
                            wordsToDelete.add(word)
                elif colour == Colour.yellow:
                    for word in possibleWords.keys():
                        if word[i] == guessWord[i]:
                            wordsToDelete.add(word)
                        elif guessWord[i] not in word:
                            wordsToDelete.add(word)

            for word in wordsToDelete:
                possibleWords.pop(word)
    return guessWord, guessCount
