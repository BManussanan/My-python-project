def remove_duplicates(t):
    x = []
    for text in t:
        if text not in x:
            x.append(text)
    return x

print(remove_duplicates([1, 2, 3, 2, 1, 2, 3, 4]))
print(remove_duplicates(['a', 'b', 'c', 'e', 'f'])) 
print(remove_duplicates([2, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3]))  