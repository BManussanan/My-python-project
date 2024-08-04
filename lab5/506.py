num = int(input())
summ = 0
i = 0
if num % 9 == 0 :
    while(True):
        if num == 0:
            break
        i = num % 10
        num = num//10
        summ += i
    print(f'Yes {summ}')
else:
    print(f'No {num%9}')