while True:
    user_choise = input("Hey, please tell me do you earn a global salary or an hourly salary? [global/hourly]:- ")
    if user_choise == 'global':
        global_salary = int(input("Please enter you global monthly salary:- "))
        miss_days = int(input("Did you miss a few work days this month? [There are 22 working days per month]:- "))
        day_salary = global_salary / 22
        salary = day_salary * (22 - miss_days)


        print(f"you salary for this month is - {salary} shekels, you miss {miss_days} days this month")














