target = int(input('Enter a target (4-digit integer): '))
guess = int(input('Enter your guess (4-digit integer): '))
pos = 0
digit = 0
tar = target
gue = guess
out1 = ''
out2 = ''
while(tar != 0 and gue != 0):
    i = tar % 10
    x = gue % 10
    if i == x :
        pos += 1
    tar //= 10 
    gue //= 10
tar = target
while(tar > 0):
    i = tar % 10
    g = guess
    while(g > 0):
        x = g % 10
        if i == x :
            digit += 1
            break
        g //= 10
    tar //= 10
if pos == 4 :
    print('Congratulations, you just mastered my mind!!')
else:
    digit = digit - pos
    if pos == 0:
        out1 = 'No positions'
    elif pos == 1:
        out1 = 'One position'
    elif pos == 2:
        out1 = 'Two positions'
    elif pos == 3:
        out1 = 'Three positions'
    elif pos == 4:
        out1 = 'Four positions' 
        
    if digit == 0:
        out2 = 'no digits'
    elif digit == 1:
        out2 = 'one digit'
    elif digit == 2:
        out2 = 'two digits'
    elif digit == 3:
        out2 = 'three digits'
    elif digit == 4:
        out2 = 'four digits' 
    print(f'{out1} correct, {out2} correct')

    

