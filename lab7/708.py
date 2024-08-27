import math
def pytha(A,number):
    j = 1
    i = 0
    total = 0
    while j < number:
        total = math.pow(A,2) + math.pow(j,2)
        j += 1
        if total == math.pow(number,2):
            i += 1
    return i/2

num = int(input())
a = 1
summ = 0
if num > 0:
    while a < num:
        summ += pytha(a,num)
        a+=1
    print(f'{summ:.0f}')
