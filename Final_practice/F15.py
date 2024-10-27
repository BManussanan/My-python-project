text = str(input())
t = text.split(' ')
ex = ['for', 'and', 'with', 'of']
result = []
for te in t :
    if te in ex:
        result.append(te)
    else:
        result.append(te.capitalize())
output = ' '.join(result)
print(output)