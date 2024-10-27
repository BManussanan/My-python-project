text = str(input())
c = int((len(text)/2))
if len(text) % 2 == 0:
    first = text[c-1::-1]
    last = text[:c-1:-1]
    print(first+last)
else:
    if len(text) == 1:
        print(text)
    else:
        first = text[c-1::-1]
        last = text[:c:-1]
        print(first + text[c] + last)