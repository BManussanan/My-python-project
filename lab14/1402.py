def cloth_size(width_list):
    result = {'S':0, 'M':0, 'L':0}
    for w in width_list:
        if w <= 36:
            result['S'] += 1
        elif w > 36 and w <= 44:
            result['M'] += 1
        elif w > 44:
            result['L'] += 1
    return result
print(cloth_size([50, 44, 40, 48]))