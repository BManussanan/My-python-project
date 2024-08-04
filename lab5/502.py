import math
hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))
total = 0 
while(True):
    if hours < 0 or hours > 20 or minutes < 0 or minutes > 59 or (hours == 20 and minutes > 0):
        print('Invalid time.')
        break        
    else:
        time = hours+math.ceil(minutes/60)
        if buyAmt >= 3001 :
            print('No charge, thank you.')
        elif time <= 2:
            print('No charge, thank you.')
        else:
            if time <= 4:
                if buyAmt >= 300 and buyAmt <= 3000:
                    print('No charge, thank you.')
                else :
                    total = (time-2)*20
                    print(f'Total amount due is {total} Baht, thank you.')      
            else:
                if buyAmt >= 300 and buyAmt <= 3000:
                    total = (time-4)*50
                    print(f'Total amount due is {total} Baht, thank you.')       
                else:
                    total = 40 + (time-4)*50
                    print(f'Total amount due is {total} Baht, thank you.')
        break