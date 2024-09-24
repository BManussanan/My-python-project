def factor_count(n):
    i = 1
    x = 0
    while i<=n:
        if n%i==0:
            x+=1
        i+=1
    return x
n = int(input("Enter n: "))
c = factor_count(n)
print(c)