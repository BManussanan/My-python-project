x = []
while True:
    num = int(input())
    if num == -1:
        break
    if num > 0:
        x.append(num)
i = 1
a = [x[0]]
while i < len(x):
    if x[i] < x [i-1]:
        x.remove(x[i])
    if x[i] >= x[i-1]:
        a.append(x[i])
    i += 1
print(a)