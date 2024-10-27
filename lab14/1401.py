def count_char(word):
    count = {}
    for w in word.lower():
        c = 0
        if w.isalpha():
            for t in word.lower():
                if w == t:
                    c += 1
            if w not in count:
                count[w] = c
    return count
print(count_char('Hello, There'))