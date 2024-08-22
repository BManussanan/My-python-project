num = int(input())
if num > 0:
    while True:
        if num == 0 : 
            break
        print(num%10) 
        num = num // 10 
else:
    print('ERROR')