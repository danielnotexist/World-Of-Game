score = 0
print("***** Welcome to Quic Game! *****")

# Question 1
user_answer = input("What is your favorite programming language? ").lower()
while user_answer != 'python':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

# Question 2
user_answer = input("Who is the it project manager of seetech sulotion? ").lower()
while user_answer != 'mida':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

# Question 3
user_answer = input("Who is the original skak? ").lower()
while user_answer != 'bar':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

print(f"you answer {score} times currectly!")


