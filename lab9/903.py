def nb_year(p0, percent, aug, p):
    i = 0
    x = 0
    while True:
        x = int(p0+(p0*(percent/100))+aug)
        i+=1
        if x >= p:
            break
        p0 = x
    return i
print( nb_year(1000, 2, 30, 1150) )