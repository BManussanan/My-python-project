text = str(input())
t = text.split(',')
i = 0
output = ''
while i < len(t):
    output += '"' + t[i].strip(' ') + '"'
    if i == len(t)-1:
        output += ''
    else:
        output += ','
    i += 1
print(output)