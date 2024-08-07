target = 72
x = 0
while(True):
    num = int(input('Enter your guess: '))
    x += 1
    if(num >= 0 and num <= 100):
        if num < target :
            print('Sorry, your guess is too low.')
        elif num > target:
            print('Sorry, your guess is too high.')
        else:
            print('Congratulations, your guess is correct.')
            break
    else:
        print('Sorry, your guess is out of range.')
print(f'Total number of guesses is {x}.')