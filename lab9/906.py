def alternating_sum(n):
    i = 1
    summ = 0
    while i<= n:
        if i%2 == 0:
            summ -= i
        else:
            summ += i
        i += 1
    return summ
n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,alternating_sum(n)))