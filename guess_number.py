import random

def print_random():
    n = random.randrange(1 ,10)
    guess = int(input("Enter any number: "))
    while n != guess:
        print(guess-n)
        print(n)
