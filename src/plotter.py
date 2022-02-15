from audioop import avg
import matplotlib.pyplot as plt
import json
import os
import numpy as np

if __name__ == '__main__':
    latestVersionNumber = int(input("Enter latest version number: "))
    if latestVersionNumber < 0:
        print("Error: invalid version number!")
        exit()

    performance = {}
    avgGuessCounts = [None] * (latestVersionNumber + 1)
    maxGuessCounts = [None] * (latestVersionNumber + 1)

    for versionNumber in range(0, latestVersionNumber + 1):
        dirname = os.path.dirname(__file__)
        jsonFilePath = os.path.join(
            dirname, '..', 'data', 'performance', 'version' + str(versionNumber) + '.json')
        with open(jsonFilePath, 'r') as jsonFile:
            performance[versionNumber] = json.load(jsonFile)

            avgGuessCounts[versionNumber] = []
            maxGuessCounts[versionNumber] = []
            for wordLength in performance[versionNumber]:
                avgGuessCounts[versionNumber].append(
                    performance[versionNumber][wordLength]["avgGuessCount"])
                maxGuessCounts[versionNumber].append(
                    performance[versionNumber][wordLength]["maxGuessCount"])

    wordLengths = [x for x in range(1, 21)]

    # Plot word length v/s average guess counts
    plt.xlabel('Word Length')
    plt.ylabel('Average Guesses Needed')
    plt.xticks([x for x in range(0, 21, 2)])

    for versionNumber in range(0, latestVersionNumber + 1):
        plt.plot(wordLengths, avgGuessCounts[versionNumber])
    plt.show()

    # Plot word length v/s max guess counts
    plt.xlabel('Word Length')
    plt.ylabel('Max Guesses Needed')
    plt.xticks([x for x in range(0, 21, 2)])

    for versionNumber in range(0, latestVersionNumber + 1):
        plt.plot(wordLengths, maxGuessCounts[versionNumber])
    plt.show()
