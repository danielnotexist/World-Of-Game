print("*** Hello and welcome to BMR Calculator! ***")
while True:
    age = int(input("please enter you age:- "))
    height = int(input("pleae enter your height:- "))
    weight = int(input("please enter your weight:- "))
    bmr = int((age * 5) - (height * 6.25) + (weight * 10))
    print(f"your BMR is 1{bmr}")
    again = input("wanna calc again?[Y/N]: - ").lower()
    if again == "y": continue
    else: break