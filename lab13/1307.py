s = str(input())
st = s.split('x')
m = int(st[0])
n = int(st[1])
table = ''

point = []
num = int(input())
for i in range(num):
    po = str(input())
    point.append(po.split(','))
p = []
for pp in point:
    p.append([int(pp[0]),int(pp[1])])

for i in range(m):
    for j in range(n):
        if [i, j] in p:
            table += '*'
        else:
            c = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        continue
                    a = i + x
                    b = j + y
                    if 0 <= a < m and 0<= b < n and [a,b] in p:
                        c += 1
            table += f'{c}'
    table += '\n'
print(table)