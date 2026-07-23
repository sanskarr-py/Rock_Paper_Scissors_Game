import random

print("Welcome to Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

while True:

    user = input("Enter rock, paper or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer:", computer)

    #Tie case
    if user ==computer:
        print("It's a tie")
        
    #your winning cases
    elif user =="rock" and computer =="scissors":
        print("You win")
        
    elif user =="paper" and computer =="rock":
        print("You win")
        
    elif user =="scissors" and computer =="paper":
        print("You win")
        
    #computer winning cases
    elif computer =="rock" and user =="scissors":
        print("Computer wins")
        
    elif computer =="paper" and user =="rock":
        print("Computer wins")
        
    elif computer =="scissors" and user =="paper":
        print("Computer wins")
        
    #Invalid input
    else:
        print("Invalid Input")
        
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break