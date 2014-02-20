#Backward
#Challenge

word = input("Type the word: ")

print(word)

backward = ""
counter = len(word)

while counter != 0:
    backward += word[counter-1]
    counter -= 1

print(backward)

input("\nPress Enter to quit")
