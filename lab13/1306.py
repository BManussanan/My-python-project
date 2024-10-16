def check_order(l):
    if len(l) == 0:
        return 'The list is empty.'
    else:
        x = l[0]
        sa = l[0]
        s = 0
        out = ''
        for ls in l:
            if ls == sa:
                sa = ls
                s += 1
        i = 1
        while i < len(l):
            if l[i] < x:
                x = l[i]
                out += 'i'
            elif l[i] > x:
                x = l[i]
                out += 'd'
            i += 1
        if s == len(l):
            return 'The list is in non-increasing and non-decreasing order.'
        elif out.count('d') == 0:
            return 'The list is in non-increasing order.'
        elif out.count('i') == 0:
            return 'The list is in non-decreasing order.'
        else:
            return 'The list is in random order.'

n = []
while True:
    num = int(input('Enter a number (-1 to end): '))
    if num == -1:
        break
    if num >= 0 and num <= 100:
        n.append(num)
    else:
        print('Number is out of range.')
    
print('-----')

print('Original list:')
print(n)
print(check_order(n))     