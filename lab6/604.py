i = 0
total1 = 0
total2 = 0
while(i < 10):
    i += 1
    print(f'Frame # {i}')
    pin = int(input('  Number of pins down: '))
    while pin != 10:
        print(f'Frame # {i}')
        total1 = int(input(f'  Number of pins down (0-{10-pin}): '))
        total2 += total1
        break
    total2 += pin
print(f'Total score is {total2}')


