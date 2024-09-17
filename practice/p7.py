data = []
while True:
    text = str(input())
    if text == '':
        break
    data.append(text)
for i in range(len(data)):
    maxx = 0
    maxx_text = ''
    for d in data:
        if len(d) > maxx:
            maxx = len(d)
            maxx_text = d
print(maxx_text)