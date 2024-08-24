num = int(input('Please input number: '))
i = 0
if num > 0:
    while num > 0:
        if num % 2 == 0:
            print(num)
            num = num//2
        else:
            print(num)
            num = num -1
        if num == 0:
            print(0)
        i += 1
if i == 1:
    print(f'{i} step')
else:
    print(f'{i} steps')

        



