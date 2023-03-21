# https://repl.it/@appbrewery/rock-paper-scissors-end
from ArtFile import rock, paper, scissors
from random import randint

art = [rock, paper, scissors]

user_choice = int (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n") )
computer_choice = randint(0, 2)

print(art[user_choice])
print("Computer chose:")
print(art[computer_choice])

if user_choice >= 3 or user_choice <= 0:
    print("You typesd an invalid number, you lose!")

elif user_choice > computer_choice:
    if computer_choice == 0 and user_choice == 2: # if computer chose Rock and user chose Scissors
        print("You lose")
    else:   # else when computer chose Paper or Rock and user chose Scissors or Paper the user will Lose.
        print("You win!")

elif user_choice < computer_choice:
     if computer_choice == 2 and user_choice == 0:  # if computer chose Scissors and user chose Rock
         print("You win!")
     else:  # else when computer chose Scissors or Paper and user chose Paper or Rock the user will Lose.
         print("You lose")

else:
    print("It's a draw.")