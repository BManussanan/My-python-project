import math
h = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))
time = (h*60)+m
round_time = math.ceil(time/60)
if m > 59 or h > 23 or m < 0 or h < 0:
    print("Input Error!")
else:
    if time <= 15:
        print("No charge, thanks.")
    elif 1 <= round_time < 3:
        total  = 10  
        print(f"Total amount due is {total} Bahts.")
    else :
        total = 10*(round_time-1)
        print(f"Total amount due is {total} Bahts.")
