text = str(input())
t = ''.join(text.split(' '))
source = str(input())
s = ''.join(source.split(' '))
descryp = str(input())
code = {}
output = ''
if len(s) <= len(t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if t[j] not in code.values():
            code[s[i]] = t[j]
            i += 1
            j += 1
        else:
            j += 1

for d in descryp:
    if d in code.keys():
        output += code[d]
    else:
        output += d
print(output)

