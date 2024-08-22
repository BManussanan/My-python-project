multi = 1
i = 0
a = 0
num = int(input(''))
if(num <= 4000000000 and num > 0):         
    while num!=0:
        x = num%10
        if x%2 != 0:
            i += 1
        if x%2 == 0:
            multi *= x
        num = num // 10
        a += 1
    if i == a :
        print(-1)
    else:
        print(multi)