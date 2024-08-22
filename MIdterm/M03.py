day = int(input(''))
h = int(input(''))
m = int(input(''))
if day == 1:
    out1 = 'sunday'
elif day == 2:
    out1 = 'monday'
elif day == 3:
    out1 = 'tuesday'
elif day == 4:
    out1 = 'wednesday'
elif day == 5:
    out1 = 'thursday'
elif day == 6:
    out1 = 'friday'
elif day == 7:
    out1 = 'saturday'  

if h >= 1 and h <= 4 and m == 00:
    out2 = 'good-night'
elif h >= 1 and h < 4 :
    if m >= 1 and m <= 59:
        out2 = 'good-night'
elif h >= 4 and h < 12 :
    if m >= 1 and m <= 59:
        out2 = 'good-morning'
elif h > 4 and h <= 12 and m == 00 :
    out2 = 'good-morning'
elif h >= 12 and h < 18 :
    if m >= 1 and m <= 59:
        out2 = 'good-afternoon'
elif h > 12 and h <= 18 and m == 00 :
    out2 = 'good-afternoon'
elif h >= 18 and h < 22 :
    if m >= 1 and m <= 59:
        out2 = 'good-evening'
elif h > 18 and h <= 22 and m == 00:
    out2 = 'good-evening'
elif h == 22 or h == 23:
    if m >= 1 and m <= 59:
        out2 = 'good-night'
elif h == 23 and m == 00:
    out2 = 'good-night'
elif h == 00 :
    if m >= 1 and m <= 59:
        out2 = 'good-night'
    elif m == 00:
        out2 = 'good-night'

print(f'{out2}-{out1}.png')
