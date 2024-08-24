a = float(input('Enter amount: '))
total = 0
while True:
    c = input('Enter command (w for withdraw, d for deposit, e for exit): ') 
    if c != 'w' and c != 'd' and c != 'e':
        print('Invalid Command!')
    if c == 'd':
        while True :
            d = float(input('Enter deposit amount: '))
            if d <= 0 :
                print('Incorrect transactions!')
            else:
                total = a + d
                print(f'Current balance = {total:.2f}$')
                break
        a = total
    elif c == 'w':
        while True :
            w = float(input('Enter withdraw amount: '))
            if w <= 0 :
                print('Incorrect transactions!')
            elif w > a:
                print('You cannot withdraw more than the amount in your account!')
            else:
                total = a - w
                print(f'Current balance = {total:.2f}$')
                break
        a = total
    elif c == 'e':
        break
  