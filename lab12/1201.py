text = str(input())
result = ''
for t in text:
    if t in 'aeiouAEIOU':
        result += t.upper()
    else:
        result += t.lower()
print(result)
