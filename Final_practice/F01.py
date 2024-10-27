text = str(input())
bigrams = []
i = 0
x = ''

while i < len(text):
    if i + 1 < len(text):
        x = f'{text[i].lower()}{text[i+1].lower()}'
        if x not in bigrams:
            bigrams.append(x)
    i += 1

bigrams_sort = []

while True:
    if not bigrams:
        break
    b = min(bigrams)
    bigrams_sort.append(b)
    p = bigrams.index(b)
    bigrams.pop(p)

for bs in bigrams_sort:
    print(bs)