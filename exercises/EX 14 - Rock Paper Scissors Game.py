import random
options = ("rock", "paper", "scissors")
running = True
play_again = ""

print("Rock Paper Scissors Game")

while running:
    player_choice = input("Type rock, paper or scissors: ").lower()
    if player_choice not in options:
        print("Invalid guess")
    else:
        play_again = ""
        computer_choice = random.choice(options)
        if computer_choice == player_choice:
            print("Its a tie!")
        elif computer_choice == "rock" and player_choice == "scissors":
            print("You lose!")
        elif computer_choice == "paper" and player_choice == "rock":
            print("You lose!")
        elif computer_choice == "scissors" and player_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
        print(f"Player: {player_choice}")
        print(f"Computer: {computer_choice}")

        while play_again !=  "y" and play_again != "n":
            play_again = input("Play again? (y/n): ").lower()

        if play_again == "n":
            running = False
            print("Good game!")
        else:
            running = True




