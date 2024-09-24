<<<<<<< HEAD
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

#ทำได้สองแบบ
def star(wid):
    j = 0
    out = ''
    while j < wid:
        out += '* '
        j += 1
    return out

h = int(input('Enter height: '))
w = int(input('Enter width: '))
if h <= 0 or w <= 0:
    print('Invalid input, program terminates.')
else:
    i = 1
    while i <= h:
        if i%2 != 0:
            print(star(w))
        else:
            print(f' {star(w)}')
        i += 1

=======
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

#ทำได้สองแบบ
def star(wid):
    j = 0
    out = ''
    while j < wid:
        out += '* '
        j += 1
    return out

h = int(input('Enter height: '))
w = int(input('Enter width: '))
if h <= 0 or w <= 0:
    print('Invalid input, program terminates.')
else:
    i = 1
    while i <= h:
        if i%2 != 0:
            print(star(w))
        else:
            print(f' {star(w)}')
        i += 1
>>>>>>> ac70314fe3125d1d70e3cbe5e348b59f65810e8e
