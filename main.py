print("**** Hello! welcome to the World Of Game! *****")
options = ["1", "2", "3"]
while True:
    print('List of games:\n'
    '[1] Guess the number\n'
    '[2] Quiz Game\n'
    '[3] Rock Paper Scissors\n'
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

    if user_input not in options:
        continue
print("Thanks for playing my World Of Games! Bye!")
