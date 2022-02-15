# Tests the performance (number of guesses needed) of the bot

from turtle import pos
from guesser import guesser
import matplotlib.pyplot as plt
import json
from copy import copy
import os

versionNumber = 0

if __name__ == '__main__':
    with open('data/dictionary.txt', 'r') as f:
        minWordLength = 1
        maxWordLength = 20
        # iterating over words of lengths from minWordLength to maxWordLength
        performance = {}  # key : val = word length : average number of guesses
        for wordLength in range(minWordLength, maxWordLength + 1):
            maxGuessCount = 0
            print(f'wordLength = {wordLength}')
            totalGuessCount = 0
            numWords = 0
            possibleWords = {}
            for word in f:
                w = word.strip()
                if len(w) == wordLength:
                    possibleWords[w] = -1

            f.seek(0)
            for word in f:
                w = word.strip()
                if len(w) == wordLength:
                    numWords += 1
                    targetWord = w
                    guessWord, guessCount = guesser(
                        wordLength, targetWord, copy(possibleWords))
                    maxGuessCount = max(maxGuessCount, guessCount)
                    totalGuessCount += guessCount

            if numWords == 0:
                print(f'numWords = {numWords}, wordLength = {wordLength}')

            performance[wordLength] = {}
            performance[wordLength]['avgGuessCount'] = totalGuessCount / numWords
            performance[wordLength]['maxGuessCount'] = maxGuessCount
            print(
                f'Average number of guesses: {performance[wordLength]["avgGuessCount"]}')
            print(
                f'Max number of guesses: {performance[wordLength]["maxGuessCount"]}\n')

    dirname = os.path.dirname(__file__)
    jsonFileName = os.path.join(
        dirname, '..', 'data', 'performance', 'version' + str(versionNumber) + '.json')
    with open(jsonFileName, 'w') as jsonFile:
        json.dump(performance, jsonFile)
