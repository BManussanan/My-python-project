import math
while True:
    print('<<Point a>>')
    x1 = int(input('Enter x coordinate: '))
    y1 = int(input('Enter y coordinate: '))
    print('<<Point b>>')
    x2 = int(input('Enter x coordinate: '))
    y2 = int(input('Enter y coordinate: '))
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0 :
        print('Goodbye')
        break
    eucli = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
    hori = abs(x1 - x2)
    verti = abs(y1 - y2)
    if x1 == x2 and y1 == y2:
        direct = 'nowhere'
    elif x1 == x2 and y1 < y2:
        direct = 'north'
    elif x1 == x2 and y1 > y2:
        direct = 'south'
    elif y1 == y2 and x1 < x2:
        direct = 'east'
    elif y1 == y2 and x1 > x2:
        direct = 'west'
    elif x1 < x2 and y1 > y2 :
        direct = 'south-east'
    elif x1 > x2 and y1 > y2 :
        direct = 'south-west'
    elif x1 < x2 and y1 < y2 :
        direct = 'north-east'
    elif x1 > x2 and y1 < y2 :
        direct = 'north-west'
    print(f'Distance between ({x1}, {y1}) and ({x2}, {y2}):')
    print(f'Euclidean distance is {eucli:.2f}.')
    print(f'Horizontal distance is {hori:.0f}.')
    print(f'Vertical distance is {verti:.0f}.')
    print(f'We are going {direct}.')