def prime(num):
    i = 1
    x = 0
    while i <= num:
        if num%i == 0:
            x += 1
        i += 1
    if x == 2:
        return f'{num} is a prime number.'
    else:
        return f'{num} is not a prime number.'


while True:
    number = int(input('Enter a number: '))
    if number == 0:
        print('End of program, goodbye.')
        break
    if number <= 1:
        print('Invalid input, try again.')
        continue
    print(prime(number))
