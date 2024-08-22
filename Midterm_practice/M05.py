number = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))
x = 0
count = 0
if number >= 0 and (digit >= 0 and digit <= 9):
    while number != 0:
        x = number % 10
        if x == digit:
            count+=1
        number = number // 10 
    if count == 1:
        print(f'Digit {digit} occurs {count} time.')
    else:
        print(f'Digit {digit} occurs {count} times.')
else:
    if number < 0:
        print('Invalid number.')
    if digit < 0 or digit > 9:
        print('Invalid digit.')


