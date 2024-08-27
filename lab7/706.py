def star(wid,x):
    j = 0
    while j < wid:
        if x%2 != 0:
            print('* ',end='')
        else:
            print(' *',end='')
        j += 1

h = int(input('Enter height: '))
w = int(input('Enter width: '))
if h <= 0 or w <= 0:
    print('Invalid input, program terminates.')
else:
    i = 1
    while i <= h:
        star(w,i)
        print()
        i += 1
