import math
num = int(input())
i = 1
x = 0
a = 0
minn = math.inf
summ = 0
if num > 0:
    while i<num :
        x = num//i
        a = x * i
        if a == num:
            summ = x + i
            if summ < minn:
                minn = summ
        i += 1
if minn == math.inf:
    print(num)
else :
    print(int(minn))

