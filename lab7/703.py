def abc(x):
    result = ''
    a = 0
    while a < x :
        ch = ord('A') + a
        result += chr(ch)
        a += 1
    return result      
num = int(input('Enter a number: '))
if num <= 0 or num > 26:
    print('Invalid input, program terminates.')
else:
    i = 1
    while i < num :
        res = abc(i)
        print(res)
        i += 1
    i = num
    while i >= 1:
        res = abc(i)
        print(res)
        i -= 1
        
    
    