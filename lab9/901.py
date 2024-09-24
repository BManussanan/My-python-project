def check_prime(n):
    i = 1
    x = 0
    while i<=n:
        if n%i == 0:
            x+=1
        i+=1
    if x == 2:
        return True
    else:
        return False
n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")