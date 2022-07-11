
import random as rd

# Set variables
counter = 0
tries = 5
print("******* Welcome to GuessGame! *******")
start_target = int(input("Please enter the start target number of range:- "))
last_target = int(input("Please enter the last target number of range:- "))
target = rd.randint(start_target, last_target)
print(f"You have only {tries} chance to guess the number between {start_target} to {last_target}!")
user_choose = int(input("please enter your guess:- "))
while user_choose != target:
    if user_choose < target:
        print("Too Low!")
    else:
        print("Too Hihg!")
    counter += 1
    user_choose = int(input("please enter your guess:- "))
    if counter == tries:
        break
if counter <= tries:
    print(f"You Did it! in {counter} Times!")
else:
    print(" you try maximum time! sorry!")
