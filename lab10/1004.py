def find_mode(l):
    maxx = l.count(l[0])
    mode  = []
    for x  in l:
        c = l.count(x)
        if c > maxx:
            maxx = c
            mode = [x]
        elif c == maxx:
            if x not in mode:
                mode.append(x)
    mode.sort()
    for modes in mode:
        print(modes)

i = 0
score = []
while i < 20:
    num = int(input('Enter score: '))
    if num > 10 or num < 0:
        print('Score is out of range.')
    else:
        score.append(num)
        i += 1
print('-----')
print('Original list:')
print(score)
print('Mode of scores:')
find_mode(score)
