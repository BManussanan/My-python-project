import math
number = []
maxx = -math.inf
num = []
while True:
    x = int(input())
    if x == 0:
        break
    number.append(x)
for i in range(len(number)):
    for j in range(i,len(number)):
        num = number[i:j+1]
        if sum(num) > maxx:
            maxx = sum(num)
print(maxx)