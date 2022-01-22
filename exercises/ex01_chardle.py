"""EX01 - Chardle - A cute step toward Wordle."""

word: str = str(input("Enter a 5-character word."))
character: str = str(input("Enter a single character."))
n: int = 0
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    quit()
if len(character) != 1:
    print("Error: Character must be a single character.")
    quit()
print("Searching for " + (character) + " in " + (word))
if (character) == (word)[0]:
    print((character) + " found at index 0")
    n = n + 1
if (character) == (word)[1]:
    print((character) + " found at index 1")
    n = n + 1
if (character) == (word)[2]:
    print((character) + " found at index 2")
    n = n + 1
if (character) == (word)[3]:
    print((character) + " found at index 3")
    n = n + 1
if (character) == (word)[4]:
    print((character) + " found at index 4")
    n = n + 1
if n == 0:
    print("No instances of d found in" + (word))
else: 
    print(str(n) + " instances of e found in " + (word))

__author__ = "730510546"