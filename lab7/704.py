def result(f):
    if f == 0 or f == 1:
        return ' = 1'
    else:
        j = 1
        out = ''
        while j < f:
            out += f' x {f-j}'
            j += 1
        return f' = {f}{out}'

num = int(input('Enter a number: '))
i = 0
fax = 0
total = 1
if num < 0:
    print('Invalid input, program terminates.')
else:
    while i <= num:
        print(f'{fax}!{result(fax)} = {total}')
        i += 1
        fax += 1
        total = total * i
