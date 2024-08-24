def abc(x):
    a = 0
    while a < x:
        ch = ord('A') + a
        print(chr(ch), end='')
        a += 1
    print()

num = int(input('Enter a number: '))
if num <= 0 or num > 26:
    print('Invalid input, program terminates.')
else:
    i = 1
    while i <= num :
        abc(i)
        i += 1