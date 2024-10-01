text = str(input())
symbol = '- _ = . $'
output = ''
i = 0
while i < len(text):
    if text[i] in symbol:
        i += 1
    if text[i]  not in symbol:
        break
        

if text[i] not in symbol and i < len(text):
    output += text[i].lower()
    i += 1

while i < len(text):
    if text[i] in symbol:
        if i+1 < len(text) and text[i+1] not in symbol:
            output += text[i+1].upper()
            i += 2
        else:
            i += 1
    else:
        output += text[i].lower()
        i += 1
print(output)