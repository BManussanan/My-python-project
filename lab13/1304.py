def count_sunday(m,da,fs):
    month31 = [1,3,5,7,8,10,12]
    month30 = [4,6,9,11]
    month28 = [2]
    er_m = False
    er_day = False

    if m[0] > 12 or m[1] > 12 or m[0] < 1 or m[1] < 1:
        er_m = True

    if m[0] in month31 and (da[0] > 31 or da[0] < 1):
        er_day = True
    elif m[0] in month30 and (da[0] > 30 or da[0] < 1):
        er_day = True
    elif m[0] in month28 and (da[0] > 28 or da[0] < 1):
        er_day = True
        
    if m[1] in month31 and (da[1] > 31 or da[1] < 1):
        er_day = True
    elif m[1] in month30 and (da[1] > 30 or da[1] < 1):
        er_day = True
    elif m[1] in month28 and (da[1] > 28 or da[1] < 1):
        er_day = True
    
    if fs < 1 or fs > 7:
        er_day = True

    if er_m :
        print('Wrong Month')
    if er_day:
        print('Wrong Day')
    if er_day or er_m:
        return
    
    num_sun = 0
    if m[0] == m[1]:
        for i in range(da[0],da[1]+1):
            if (i-fs) % 7 == 0:
                num_sun += 1
    else:
        if m[0] in month31:
            x = 31
        elif m[0] in month30:
            x = 30
        elif m[0] in month28:
            x = 28
        for i in range(da[0],x+1):
            if (i-fs) % 7 == 0:
                num_sun += 1

        for i in range(m[0]+1,m[1]):
            if i in month31:
                    x = 31
            elif i in month30:
                    x = 30
            elif i in month28:
                    x = 28
            for j in range(1,x+1):
                if (j-fs) % 7 == 0:
                    num_sun += 1
        
        for i in range(1,da[1]+1):
            if (i-fs) % 7 == 0:
                num_sun += 1

    print(num_sun) 

date1 = str(input()).split('-')
date2 = str(input()).split('-')
fsunday = int(input())

date1 = [int(num) for num in date1]
date2 = [int(num) for num in date2]

if date1[1] < date2[1] or (date1[1] == date2[1] and date1[0] <= date2[0]):
    m = [date1[1],date2[1]]
    day = [date1[0],date2[0]]
else:
    m = [date2[1],date1[1]]
    day = [date2[0],date1[0]]

count_sunday(m,day,fsunday)