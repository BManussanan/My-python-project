day = input()
date = int(input())

if day == 'Sunday':
    i = 0
elif day == 'Monday':
    i = 1
elif day == 'Tuesday':
    i = 2
elif day == 'Wednesday':
    i = 3
elif day == 'Thursday':
    i = 4
elif day == 'Friday':
    i = 5
elif day == 'Saturday':
    i = 6
else:
    i = -1

if (date <= 31 and date >= 1) and (i >= 0 and i < 7):
    output = (i + (date - 1))%7
    if output == 0:
        print('Sunday')
    elif output == 1:
        print('Monday')
    elif output == 2:
        print('Tuesday')
    elif output == 3:
        print('Wednesday')
    elif output == 4:
        print('Thursday')
    elif output == 5:
        print('Friday')
    elif output == 6:
        print('Saturday')
else:
    print('ERROR')


    



