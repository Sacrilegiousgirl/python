from wordlist_5_letters import words
import random

answer = random.choice(words)

def show_hint(hint):
    print(" ".join(hint))

def appropriate_input(guess, words):
    if not guess.isalpha():
        print("Invalid input")
        return False
    elif len(guess) != 5:
        print("You must type a 5-letter word")
        return False
    elif guess not in words:
        print("This word doesnt exist in the dictionary!")
        return False
    else:
        return True

def win_message(guesses, hints):
    print()
    print("**************************************")
    print("YOU WON!")
    print(f"It took you {guesses+1} guesses to guess the right answer")
    print("Here are your guesses in emojis:")
    print()
    for hint in hints:
        print(" ".join(hint))
    print("**************************************")

def lose_message(answer, hints):
    print()
    print("**************************************")
    print("YOU LOST!")
    print(f"The answer is {answer}")
    print("Here are your guesses in emojis:")
    print()
    for hint in hints:
        print(" ".join(hint))
    print("**************************************")


if __name__ == '__main__':
    guesses = 0
    hints = []

    while guesses < 6:
        hint = ["💩"] * 5 
        guess = input("Type in your guess: ")

        if not appropriate_input(guess, words):
            continue

        for x in range(5):
            if guess[x] in answer:
                    hint[x] = "🟨"

        for i in range(5):
            if guess[i] == answer[i]:
                hint[i] = "🟩"

        hints.append(hint)
        show_hint(hint)

        if hint[0] == hint[1] == hint[2] == hint[3] == hint[4] == "🟩":
            break
        else:
            guesses += 1

    if guesses < 6:
        win_message(guesses, hints)
    else:
        lose_message(answer, hints)
       

