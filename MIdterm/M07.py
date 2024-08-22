sunday = int(input())
day = int(input())
if (sunday <= 7 and sunday >= 1) and (day >= 0 and day <=31) :
    count = (day-sunday)%7  
    if count == 1:
        print("Monday")
    elif count == 2:
        print("Tuesday")
    elif count == 3:
        print("Wednesday")  
    elif count == 4:
        print("Thursday")  
    elif count == 5:
        print("Friday")  
    elif count == 6:
        print("Saturday")  
    elif count == 0:
        print("Sunday")     
else:
    print("ERROR")
