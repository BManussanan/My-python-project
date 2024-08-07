i = 0
maxx = 0
while(True):
    num = int(input())
    if num == -1 :
        break
    if num > maxx :
        i += 1
        maxx = num
print(i)