import random

random.randint(1,100)

jackpot = random.randint(1,100)

guess = int(input("Guess kar bro:"))

counter = 1

while guess != jackpot :
    if guess<jackpot:
        print("Guess Higher")
    else:
        print("Guess lower")
    guess = int(input("Phirse guess kar bro:"))
    counter += 1


print("Sahi hai bhai.")

print("You took", counter, "attempts")