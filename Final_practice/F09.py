num = int(input())
element = []
for i in range(num):
    x = str(input())
    element.append(x)
c = num//2
output = ''
for e in element:
    n = element.count(e)
    if n > c:
        output = e
if output == '':
    print(0)
else:
    print(output)