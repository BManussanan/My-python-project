def check_format(m):
    number = '0123456789'
    if '.' in m:
        p = m.find('.')
        a = m[:p]
        b = m[p+1:]
        if m.count('.') != 1 or len(b) != 2:
            return False
    else:
        a = m
        b =''
    
    digit = 0
    comma = 0
    for i in range(len(a)):
        if a[i] == ',':
            comma += 1
            if (digit % 3 != 0 and digit > 4) or digit == 0:
                return False
            digit = 0
        else:
            if a[i] not in number:
                return False
            digit += 1

    if digit == 0 or (digit % 3 != 0 and comma > 0):
        return False
    
    return True
        
money = input()
if check_format(money) == False:
    print('ERROR')
else:
    output = money.replace(',','')
    result = float(output) + 1
    if '.' in output:
        print(f'{result:.2f}')
    else:
        print(f'{int(result)}')
    