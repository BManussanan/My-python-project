import math
text = str(input())
output = ''
i = 0
x = math.ceil(len(text)/2)
while i < x:
    output += text[i]
    i += 1
    if len(text)%2 == 0:
        if len(text)-i < len(text):
            output += text[len(text)-i]
    else:
        if len(text)-i < len(text) and i < x:
            output += text[len(text)-i]
print(output)
