def factorial(n):
    if n>=0:
        i = 1
        x = 1
        while i<=n:
            x *= i
            i +=1
        return x
n = int(input("Enter n: "))
print(f'{n}!', "=", factorial(n))