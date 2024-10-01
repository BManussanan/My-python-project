text = str(input())
symbol = '\\ / * : | " < >.'
a = text.rfind('.')
x = ''
y = '.'
if text.count('.') > 0:
    firstname = text[:a]
    lastname = text[a:len(text)]
    for f in firstname:
        if f in symbol:
            x += '_'
        else:
            x += f
    i = 1
    while i < len(lastname):
        if lastname[i] in symbol:
            y += '_'
        else:
            y += lastname[i]
        i += 1
    print(x[:15]+y[:4])
else:
    firstname = text
    for f in firstname:
        if f in symbol:
            x += '_'
        else:
            x += f
    print(x[:15])





