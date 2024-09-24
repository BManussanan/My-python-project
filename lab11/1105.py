result = str(input())
check = str(input())
c = 0
for r in result:
    if r in check:
        c += 1
print(c)
per = (c/(len(result)-2))*100
print(f'{per:.2f}')
