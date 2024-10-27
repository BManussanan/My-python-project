import math
num = int(input())
number = []
for i in range(num):
    x = int(input())
    number.append(x)
a = 0
b = 0
minn = math.inf
output = []
for n in number:
    for m in number:
        diff = abs(n - m)
        if diff != 0:          
            if diff < minn:
                minn = diff
for n in number:
    for m in number:
        diff = n-m
        if diff == minn:
            temp = [n,m]
            temp.sort()
            if temp not in output:
                output.append(temp)
for o in output:
    print(f'{o[0]} {o[1]}')


    

        