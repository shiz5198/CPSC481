#random word order program

import random

word = ["happy", "camp", "sorry", "mother", "food")

while word:
    r = random.choice(word)
    print r
    while r in word:
        word.remove(r)

input("\n\nPress the enter key to exit.")
