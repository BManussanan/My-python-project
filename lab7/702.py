def abc(x,number):
    a = number
    s = 0
    while a >= x:
        ch = ord('A') + s
        print(chr(ch), end='')
        s += 1            
        a -= 1
    print()

num = int(input('Enter a number: '))
if num <= 0 or num > 26:
    print('Invalid input, program terminates.')
else:
    i = 1
    while num >= i :
        abc(i,num)
        i += 1