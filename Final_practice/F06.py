text = str(input())
num = int(input())
if len(text) > 0:
    num = num % len(text)
    if num < 0 :
        t1 = text[:abs(num)]
        t2 = text[abs(num):]
        print(t2+t1)
    elif num > 0:
        t1 = text[-num:]
        t2 = text[:-num]
        print(t1+t2)
    else:
        print(text)