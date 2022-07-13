score = 0
print("***** Welcome to Quic Game! *****")

# Question 1
user_answer = input("What is your favorite programming language? ").lower()
while user_answer != 'python':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

# Question 2
user_answer = input("What does CPU stand for? ").lower()
while user_answer != 'central processing unit':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

# Question 3
user_answer = input("What does GPU stand for? ").lower()
while user_answer != 'graphics processing unit':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

# Question 4
user_answer = input("What does RAM stand for? ").lower()
while user_answer != 'random access memory':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

# Question 5
user_answer = input("What does PSU stand for? ").lower()
while user_answer != 'power supply':
        user_answer = input("Please try again:- ").lower()
print("Currect!")
score += 1

print(f"you answer {score} times currectly!")


