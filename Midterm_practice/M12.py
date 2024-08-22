total = 0
summ = 0
result = ''
target = 0
i = 0
while True :
    num1 = int(input())
    num2 = int(input())
    summ = num1 + num2 
    if (num1 > 6 or num1 < 1) or (num2 > 6 or num2 < 1):
        print('ERROR')
        continue
    i += 1
    if summ == 7 or summ == 11:
        result = 'W'
        break
    elif summ == 2 or summ == 3 or summ == 12:
        result = 'L'
        break
    else:
        target = summ
        while True:
            num1 = int(input())
            num2 = int(input())
            if (num1 > 6 or num1 < 1) or (num2 > 6 or num2 < 1):
                print('ERROR')
                continue
            total = num1 + num2
            i += 1
            if total == 7:
                result = 'L'
                break
            elif target == total :
                result = 'W'
                break
        break
if i == 1:
    print(f'{i} {summ} {result}')
else:
    print(f'{i} {total} {result}')




