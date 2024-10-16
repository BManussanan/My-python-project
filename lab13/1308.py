def extract_string(text):
    num = ''
    stri = ''
    number = '0123456789'
    ls = []
    i =  0
    while i < len(text):
        if text[i] in number:
            num += text[i]
        else:
            stri += text[i]
        if i+1 < len(text):
            if text[i] in num and text[i+1] not in number:
                ls.append(int(num))
                num = ''
            elif text[i] not in num and text[i+1] in number:
                ls.append(stri)
                stri = ''
        if i == len(text)-1:
            if text[i] in number:
                ls.append(int(num))
            else:
                ls.append(stri)
        i += 1
    return ls
print( extract_string("G2X3t4") )
print( extract_string("1 2 3 4 5 I love you.") )