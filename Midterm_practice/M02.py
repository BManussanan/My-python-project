print('Upper left corner coordinate:')
x = int(input('  << x axis: '))
y = int(input('  << y axis: '))
east = int(input('  << Eastern: '))
south = int(input('  << Southern: '))
print('Enter a coordinate:')
a = int(input('  << x axis: '))
b = int(input('  << y axis: '))
if a >= x and a <= x+east:
    if b <= y and b >= y-south:
        output = 'inside'
    else:
        output = 'not inside'
else:
    output = 'not inside'
print(f'>>> ({a:.2f}, {b:.2f}) is {output} the rectangle.')