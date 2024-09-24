import math
def sqrt_n_times(x, n):
    total = 0
    i = 0
    while i < n:
        total = math.sqrt(x)
        x = total
        i += 1
    return total
x = float(input())
n = int(input())
print( sqrt_n_times(x, n) )