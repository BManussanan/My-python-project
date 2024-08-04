num = int(input('Enter height: '))
i = 0
x = 0
count = 0
n = 0
s = ' '
if num > 0 :
    print(f'{1:>{num+(num-i)}}')
    while i < (num-1):
        i += 1
        count = num+(num-i)+n
        print(f'{1:>{count}}'+s*((x*2)-1)+'1'*x)
        n -= 1
        x += 2
else:
    print('')
        
