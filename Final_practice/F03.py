scale = str(input()).split(',')
num = int(input())
major = []
i = 0
while i < len(scale)-1:
    major.append(scale[i])
    i += 1
p = (num%7)-1
print(major[p])
