"""An oracle that predicts the future."""

from random import randint

input("Ask a ramdom question: ")
response: int = randint(0,3)
if response == 1:
    print("Highly likely")
elif response == 2:
        print("Ask again later")
else:
        print("No way, not a chance")
