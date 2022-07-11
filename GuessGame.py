import random as rd

# Set variables
counter = 1
tries = 5
print("******* Welcome to GuessGame! *******")

# The user selects a start number and an end number to select the range of the target number
start_target = int(input("Please enter the start target number of range:- "))
end_target = int(input("Please enter the last target number of range:- "))
target = rd.randint(start_target, end_target)
print(f"You have only {tries} chance to guess the number between {start_target} to {end_target}!")

# The user has to guess the number
user_choose = int(input("please enter your guess:- "))

# While loop to test the user input
while user_choose != target:
    if user_choose < target:
        print("Too Low!")
    else:
        print("Too Hihg!")
    counter += 1
    user_choose = int(input("please enter your guess:- "))
    if counter == tries:
        break
# End of the whille loop

if counter <= tries:
    print(f"You Did it! in {counter} Times!")
else:
    print(" you try maximum time! sorry!")
