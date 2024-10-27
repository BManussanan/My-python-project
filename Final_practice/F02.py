def father_name(f):
    vowel = ['a','e','i','o','u']
    v = 0
    i = 0
    n1 = ''
    while i < len(f):
        if f[i] in vowel:
            v += 1
        if v == 2:
            break
        n1 += f[i]
        i += 1
    if not n1:
        return f
    else:
        return n1
def mother_name(m):
    vowel = ['a','e','i','o','u']
    j = 0
    a = 0
    while j < len(m):
        if a == 1:
            break
        if m[j] in vowel:
            a += 1
        j += 1
    n2 = m[j:]
    if not n2:
        return m
    else:
        return n2
father = str(input())
mother = str(input())
print(father_name(father)+ mother_name(mother))