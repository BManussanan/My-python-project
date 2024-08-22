num = int(input())
i = 0
x = 0
if num > 0:
    summ = 0
    while(num != 0):
        i = num%10
        num = num//10
        summ += i
    while(summ > 9):
        total = 0
        while(summ != 0):
            x = summ%10
            summ = summ//10
            total += x
        summ = total
    print(f'{summ}')