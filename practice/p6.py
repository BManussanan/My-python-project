num = int(input('Enter amount of money: '))

if num >= 1000:
    x = num//1000
    print(f'1000: {x}')
    num = num%1000

if num >= 500:
    x = num//500
    print(f'500: {x}')
    num = num%500
    
if num >= 100:
    x = num//100
    print(f'100: {x}')
    num = num%100
    
if num >= 50:
    x = num//50
    print(f'50: {x}')
    num = num%50
    
if num >= 20:
    x = num//20
    print(f'20: {x}')
    num = num%20
    
if num >= 10:
    x = num//10
    print(f'10: {x}')
    num = num%10
if num >= 5:
    x = num//5
    print(f'5: {x}')
    num = num%5
if num >= 2:
    x = num//2
    print(f'2: {x}')
    num = num%2
if num >= 1:
    x = num//1
    print(f'1: {x}')
    num = num%1