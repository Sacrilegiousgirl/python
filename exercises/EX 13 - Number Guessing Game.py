import random
guesses = []
guess = 0
low = 1
high = 200
answer = random.randint(low, high)

print("Python Number Guessing Game")
print(f"Select a number between {low} and {high}")

while guess != answer:
    guess = input("Type your guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess < low or guess > high:
            print("That number is out of range")
            print(f"Select a number between {low} and {high}")
        elif guess > answer:
            print("Too high!")
            guesses.append(guess)
        elif guess < answer:
            print("Too low!")
            guesses.append(guess)
        else:
            print("YOU WIN!")
            guesses.append(guess)
            break
    else:
        print("Invalid guess")
        print(f"Select a number between {low} and {high}")
    

print("--------------RESULT----------------")
print(f"You took {len(guesses)} guesses to figure out the right answer!")
print("Your guesses:", end=" ")
for i in guesses:
    print(i, end=" ")