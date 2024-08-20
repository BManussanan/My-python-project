age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
total = 0
if age >= 15 and age <= 60 and income < 80000 and income > 0:
    if income >= 1 and income <= 30000 :
        total = income*20/100
        print(f"Your negative income tax is {total:.2f} Baht.")
    elif income > 30000 and income < 80000 :
        total = (30000*20/100)-((income-30000)*12/100)
        print(f"Your negative income tax is {total:.2f} Baht.")
else :
    if age < 15 or age > 60 :
        print("Invalid age.")
    elif income >= 80000 or income < 0:
        print("Invalid income.")
