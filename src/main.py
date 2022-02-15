from guesser import guesser
import os


def inputTargetWord(wordLength: int, possibleWords: dict) -> str:
    while True:
        targetWord = input("Enter word to be guessed:")
        if len(targetWord) != wordLength:
            print("Enter a word of 5 letters!")
        elif targetWord not in possibleWords:
            print(
                f'{targetWord} is not present in the dictionary! Please enter an English word!')
        else:
            return targetWord


if __name__ == '__main__':
    wordLength = 5
    possibleWords = {}
    # add all the words of wordLength letters in possibleWords and initialise them with a score of -1
    dirname = os.path.dirname(__file__)
    dictionaryFilePath = os.path.join(
        dirname, '..', 'data', 'dictionary.txt')
    with open(dictionaryFilePath, 'r') as f:
        for word in f:
            w = word.strip()
            if len(w) == wordLength:
                possibleWords[w] = -1

    # Take the target word as user input
    targetWord = inputTargetWord(wordLength, possibleWords)

    guessWord, guessCount = guesser(
        wordLength, targetWord, possibleWords, printGuess=True)

    print("Word:", guessWord)
    print("Number of Guesses Used:", guessCount)
