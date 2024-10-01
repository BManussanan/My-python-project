first = []
last = []
while True:
    sen = str(input())
    if sen == '-1':
        break
    p = int(sen.find('='))
    first.append(sen[:p])
    last.append(sen[p+1:])

maxx_f = 0
x = ''
for f in first:
    if len(f.strip(' ')) > maxx_f:
        maxx_f = len(f.strip(' '))

a = maxx_f

maxx_l = 0
for l in last:
    if len(l.strip(' ')) > maxx_l:
        maxx_l = len(l.strip(' '))

b = maxx_l

j =0
while j < len(first):
    print(f'{first[j].strip(' '):>{a}} = {last[j].strip(' '):<{b}}')
    j += 1




