def prime(num):
    j = 1
    p = 0
    while j <= num:
        if num%j == 0:
            p += 1
        j += 1
    if p == 2:
        return num

number = int(input('Enter positive integer: '))
if number <= 0:
    print('Invalid number.')
elif number == prime(number):
    print(prime(number))
else:
    i = 2
    while i <= number:
        x = number/i
        if number%i == 0:
            number = x
            print(prime(i))
        else:
            i += 1



        
        
        
