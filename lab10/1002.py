def accum_sum(l):
    i = 0
    summ = 0
    while i < len(l):
        summ += l[i]
        print(summ)
        i += 1
ls = []
while True:
    num = int(input('Enter a number (0 to end): '))
    if num == 0:
        break
    if num < 1 or num > 999:
        print('Number is out of range.')
    else:
        ls.append(num)
    
print('Original list:')   
print(ls)
print('Accumulative Sum:') 
accum_sum(ls)