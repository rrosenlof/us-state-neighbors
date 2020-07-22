from spellchecker import SpellChecker
import csv

spell = SpellChecker()

with open('paths.csv', newline='') as csvfile:
    neighbors = csv.reader(csvfile, delimiter=',', quotechar='|')
    words = []
    neighbors = list(neighbors)
    for n in neighbors:
        # print(n[4])
        if spell[n[4]] and len(n[4]) > 2:
            words.append(n[4])
        if spell[n[5]] and len(n[5]) > 2:
            words.append(n[5])
            

    print(words)