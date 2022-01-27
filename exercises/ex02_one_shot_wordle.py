"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730510546"
secret: str = ("python")
var: int = len(secret)
guess: str = str(input(f"What is your {var}-letter guess?"))

while len(guess) != var:
    guess = input(f"That was not {var} letters! Try again:")
if str(guess) == secret:
    i: int = 0
    outcome: str = ""
    while i < var:
        outcome += "\U0001F7E9 "
        i += 1
    print(outcome)
    print("Woo! You got it!")
    quit()
else:
    i = 0
    outcome = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            outcome = outcome + "\U0001F7E9 "
            i += 1
        else:
            present: bool = False
            count: int = 0
            while present is False and count < var:
                if guess[i] == secret[count]:
                    outcome += "\U0001F7E8 "
                    present = True
                else:
                    count += 1
            if present is False:
                outcome += "\U00002B1C "
            i += 1
    print(outcome)
    print("Not quite. Play again soon!")
    quit()