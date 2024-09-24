def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        i = 0
        summ = 0
        x = 1
        a = 1
        while i<(n-2):
            summ = a + x
            a = x
            x = summ
            i += 1
        return summ
n = int(input("Enter n: "))
print('fibo({0}) = {1}'.format (n,fibo(n)))