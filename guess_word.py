import re
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++ Welcome to the word guessing game! +++++")
print("++++++++++++++++++++++++++++++++++++++++++++++ \b")
global word
word = "hello"
display = ' _' * len(word)

def letter_position(the_word):
    w = [l for l in word]
    new_word = w.copy()
    print(w)

    for x in the_word:
        indexes = [let.start() for let in re.finditer(x, word)]
        if len(indexes) == 0:
            pass
            print(indexes)

    return ''.join(l for l in new_word)

gameover = False

while not gameover:
    print(f'\b your hint is: {display}')
    guess_word = input(f"What is your guess: ")
    if word.lower() == guess_word.lower():
        print(f"you won, the word was {word}")
        gameover = True
    elif word.lower() != guess_word.lower():
        letter_position(guess_word)
    else:
        print(word.lower(), end="")