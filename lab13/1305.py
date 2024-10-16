n = int(input())
char = str(input()).lower()
if n >= 0:
    if n == 0 :
        fibo = [1]
    elif n == 1:
        fibo = [1,1]
    else:
        fibo = [1,1]
        for i in range(2,n+1):
            fibo.append(fibo[i-1]+fibo[i-2])

    if char == 'e':
        x = []
        for i in range(0,len(fibo),2):
            x.append(fibo[i])
        total = sum(x)
        print(total)
    elif char == 'o':
        if n == 0:
            print('ERROR')
        else:
            x = []
            for i in range(1,len(fibo),2):
                x.append(fibo[i])
                total = sum(x)
            print(total)
    else:
        print('ERROR')
else:
    print('ERROR')