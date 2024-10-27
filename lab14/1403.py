program = []
variable = {}
print('Enter variables and values:')
while True:
    v = str(input())
    if v == '-1':
        break
    a = v.split(' = ')
    variable[a[0]] = a[1]
print('Enter your program:')
while True:
    p = str(input())
    if p == '-1':
        break
    for var in variable:
        temp = '{'+var+'}'
        if temp in p:
            p = p.replace(temp,variable[var])
    program.append(p)
print('Result:')
for line in program:
    print(line)