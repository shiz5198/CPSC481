#Coin Flip
#Challenge

import random

heads = 0
tails = 0
counter = 0

while counter < 100:
    coin = random.randrange(2)
    if coin == 0:
        heads += 1
    else:
        tails += 1
    counter += 1


print("\nOut of 100 flips, ", heads, "were heads and ", tails, "were tails.")
input("\n\nPress the enter key to exit.")
