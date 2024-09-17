num = int(input())
if num > 0 and num <= 1440*30:
    if num < 60:
        if num == 1:
            print(f'{num} minute')
        else:
            print(f'{num} minutes')
    elif num >= 60:
        d = num//1440
        h = (num%1440)//60
        m = num%60
        if d == 0:
            if m == 0:
                if h > 1:
                    print(f'{h} hours')
                else:
                    print(f'{h} hour')
            else:
                if h > 1 and m > 1:
                    print(f'{h} hours {m} minutes')
                elif h > 1 and m == 1:
                    print(f'{h} hours {m} minute')
                elif h == 1 and m > 1:
                    print(f'{h} hour {m} minutes')            
                else:
                    print(f'{h} hour {m} minute')
        elif d == 1:
            if h == 0:
                if m > 1:
                    print(f'{d} day {m} minutes')
                elif m == 0:
                    print(f'{d} day')
                else:
                    print(f'{d} day {m} minute')
            elif m == 0:
                if h > 1:
                    print(f'{d} day {h} hours')
                elif h == 0:
                    print(f'{d} day')                
                else:
                    print(f'{d} day {h} hour')            
            else:
                if h > 1 and m > 1:
                    print(f'{d} day {h} hours {m} minutes')
                elif h > 1 and m == 1:
                    print(f'{d} day {h} hours {m} minute')
                elif h == 1 and m > 1:
                    print(f'{d} day {h} hour {m} minutes')            
                else:
                    print(f'{d} day {h} hour {m} minute')
        else:
            if m == 0:
                if h > 1:
                    print(f'{d} days {h} hours')
                elif h == 0:
                    print(f'{d} days')                 
                else:
                    print(f'{d} days {h} hour')
            elif h == 0:
                if m > 1:
                    print(f'{d} days {m} minutes')
                elif m == 0:
                    print(f'{d} days')                 
                else:
                    print(f'{d} days {m} minute') 
            else:
                if h > 1 and m > 1:
                    print(f'{d} days {h} hours {m} minutes')
                elif h > 1 and m == 1:
                    print(f'{d} days {h} hours {m} minute')
                elif h == 1 and m > 1:
                    print(f'{d} days {h} hour {m} minutes')            
                else:
                    print(f'{d} days {h} hour {m} minute')

    