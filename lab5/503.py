i = 0
total = 0
while(True):
    num = int(input('Enter number: '))
    if num < 0 :
        break
    if num % 2 != 0:
        total += 1
i += 1
print(f'Received {total} odd numbers')