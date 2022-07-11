import random as rd
def rockpaperscissors():
    # The user need to select from the list
    print("***** Welcome to rock paper scissors game! *****")
    user_choise = input("Please select from the list: [rock, paper, scissors]:- ").lower()

    # Set variables.
    possible_choise = ["rock", "paper", "scissors"]
    computer_choise = rd.choice(possible_choise)
    print(f"you choise {user_choise}, ther computer choise {computer_choise}")

    # Check the user input and the computer inpurt and compare between them.
    if  user_choise == computer_choise:
        print("its tie! nobody win!")
    elif user_choise == "rock":
        if computer_choise == "paper":
            print("you lose! paper cover rock!")
        else:
            print("you won! rock smash scissors!")
    elif user_choise == "paper":
        if computer_choise == "rock":
            print("you won! paper cover rock!")
        else:
            print("you lose! scissors cut scissors")
    elif user_choise == "scissor":
        if computer_choise == "rock":
            print("you lose! rock smash scissors!")
        else:
            print("you win! scissors cut paper!")

