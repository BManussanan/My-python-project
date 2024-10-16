num = int(input())
money = []
for i in range(num):
    x = int(input())
    money.append(x)
change = int(input())
money.sort(reverse=True)
c = change
for m in money:
    a = change // m
    print(f'{m}: {a}')
    change %= m



