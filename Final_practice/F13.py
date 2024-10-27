number = { 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:''}
number_10_20 = {10:'ten',11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19: 'nineteen',20:'twenty'}
num2 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',0:''}
nnumber = input()

if nnumber.isdigit() and 0 <= int(nnumber) < 999 and nnumber != '':
    num = int(nnumber)
    if num == 0:
        print('zero')
    elif num < 10:
        print(number[num])
    elif num <= 20:
        print(number_10_20[num])
    elif num < 100:
        x = num//10
        y = num%10
        if y == 0:
            print(f'{num2[x]}')
        else:
            print(f'{num2[x]}-{number[y]}')
    else:
        hun = num//100
        n = num%100
        t = f'{number[hun]}-hundred'
        if n != 0:
            if n < 10:
                t += f'-{number[n]}'
            elif n <= 20:
                t += f'-{number_10_20[n]}'
            else:
                tens = n // 10
                unit = n%10
                if unit == 0:
                    t += f'-{num2[tens]}'
                else:
                    t += f'-{num2[tens]}-{number[unit]}'
        print(t)
else:
    print('ERROR')