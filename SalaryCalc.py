while True:
    user_choise = input("Are you interested in calculating by the hour or globally? [global/hour]:- ")
    if user_choise == 'global':
        global_salary = int(input("Please enter you global monthly salary:- "))
        miss_days = int(input("Did you miss a few work days this month? [There are 22 working days per month]:- "))
        day_salary = int(global_salary / 22)
        salary = int(day_salary * (22 - miss_days))
        print(f"you salary for this month is - {salary}₪ or {day_salary}₪ every day.")
        while True:
            user_continue = input("Wanna calculate again? [Y/N]:- ").lower()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                quit()
            else:
                continue

    elif user_choise == 'hour':
        hour_salary = int(input("Please enter you global hourly salary:- "))
        hour_per_day = int(input("Please enter how much hours you work per day:- "))
        day_per_week = int(input("Please enter how much days you work per week:- "))
        calc_salary = int(hour_salary * hour_per_day * day_per_week * 4.2)
        hour_salary = print(f"You salary for this month is - {calc_salary}₪, per day - {hour_salary * hour_per_day}₪.")
        while True:
            user_continue = input("Wanna calculate again? [Y/N]:- ").lower()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                quit()
            else:
                continue















