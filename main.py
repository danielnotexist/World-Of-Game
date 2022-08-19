print("**** Hello! welcome to the World Of Game! *****")
options = ["1", "2", "3", "4", "5"]
while True:
    print('List of games:\n'
    '[1] Guess the number\n'
    '[2] Quiz Game\n'
    '[3] Rock Paper Scissors\n'
    '[4] Calculator BMR\n'
    '[5] Salary Calcolator\n'
    '[Q] to Quit the World Of Games.')
    user_input = input('Please choose the game you want to play or enter q to quit:- ').lower()
    if user_input == "q":
        break

    elif user_input == "1":
        from GuessGame import guessgame
        guessgame()

    elif user_input == "2":
        from QuizGame import quizgame
        quizgame()

    elif user_input == "3":
        from RockPaperScissors import rockpaperscissors
        rockpaperscissors()

    elif user_input == "4":
        from calc_bmr import bmr_calc
        bmr_calc()

    elif user_input =="5":
        from SalaryCalc import salary_calc
        salary_calc()

    if user_input not in options:
        continue
print("Thanks for playing my World Of Games! Bye!")
