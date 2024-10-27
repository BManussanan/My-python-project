f = str(input())
element = str(input())
table = {}
t = ''
n = ''
i = 0
while i < len(f):
    if f[i].isalpha():
        if f[i].isupper():
            if t != '':
                if n == '':
                    n = '1'
                if t in table:
                    table[t] += int(n)
                else:
                    table[t] = int(n)
            t = f[i]
            n = ''
        else:
            t += f[i]
    else:
        n += f[i]
    i += 1
if t != '':
    if n == '':
        n = '1' 
    if t in table: 
        table[t] += int(n)
    else:
        table[t] = int(n)
if element in table: 
    output = table[element]
else:
    output = 0
print(output)
