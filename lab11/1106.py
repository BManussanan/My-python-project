text = str(input())
vowel = 'aeiou'
output = ''
i = 0
while i < len(text):
    output += text[i]
    if  text[i] in vowel:
        if i+2<len(text) and text[i+1] == 'p' and text[i+2] == text[i]:
            i += 2
        else:
            i + 1
    else:
        i += 1
print(output)

