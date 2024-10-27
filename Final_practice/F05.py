import math
text = str(input()).lower()
maxx = -math.inf
c = 0
for t in text:
    if t.isalpha():
        if ord(t) > maxx:
            c += 1
            maxx = ord(t)
        else:
            break
print(c)