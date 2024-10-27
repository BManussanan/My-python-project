import math
num = int(input())
zombie = str(input()).split(' ')
total = 0
x = 0
count_gun = []
for z in zombie:
        x += math.ceil(int(z) / num)
        total = x
        count_gun.append(str(x))
print(total)
print(' '.join(count_gun))