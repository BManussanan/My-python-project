num = int(input('Please input number: '))
x = 0
origin_number = num
renum = 0
while num > 0:
    x = num%10
    renum = (renum*10)+x
    num = num//10
if origin_number == renum:
    print('True')
else:
    print('False')