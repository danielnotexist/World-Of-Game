import random as rd
user_choise = input("please choise [rock,paper,scissor")
possible_choise = ["rock", "paper", "scissor"]
computer_choise = rd.choice(possible_choise)
print(f"you choise {user_choise}, ther computer choise {computer_choise}")
if  user_choise == computer_choise:
    print("its tie! nobody win!")
elif user_choise == "rock":
    if computer_choise == "paper":
        print("you lose! paper cover rock!")
    else:
        print("you won! rock smash scissor!")
elif user_choise == "paper":
    if computer_choise == "rock":
        print("you won! paper cover rock!")
    elif:
        print("you lose! scissor cut scissor")
elif user_choise == "scissor":
    if computer_choise == "rock":
        print("you lose! rock smash scissor!")
    elif:
        print("you win! scissor cut paper!")

