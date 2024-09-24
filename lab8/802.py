def digit(num):
    x = num%10
    return x
def tens(num):
    num = num//10
    x = num%10
    return x 
def hundreds(num):
    num = num//100
    x = num%10
    return x
def thousands(num):
    num = num//1000
    x = num%10
    return x
def sum_digits(num):
    x = 0
    summ = 0
    while num>0:
        x = num%10
        summ += x
        num = num//10
    return summ

n   = int(input('Enter a number (0 to 9999): '))
print(f'Digit place is {digit(n)}.')
print(f'Tens place is {tens(n)}.')
print(f'Hundreds place is {hundreds(n)}.')
print(f'Thousands place is {thousands(n)}.')
print(f'Sum of all digits is {sum_digits(n)}.')