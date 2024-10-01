text = str(input())
correct = []
while True:
    x = str(input())
    if x == '0':
        break
    if x not in correct:
        if x in text:
            correct.append(x)
print(correct)
out = ''
for t in text:
    if t in correct:
        out += t
    else:
        out += '-'
print(out)
