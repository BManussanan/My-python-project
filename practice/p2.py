import math
num = int(input('Enter Binary digits: '))
x = 0
i = 0
b = 0
total = 0
while num != 0:
    x = num%2
    b = x*math.pow(2,i)
    i += 1
    total += b
    num = num//10
print(f'{total:.0f}')