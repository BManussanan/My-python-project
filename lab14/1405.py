import math
person = {}
number = {}
while True:
    i = 1
    p = str(input())
    if p == 'end':
        break
    temp = p.split(' ')
    a = temp[0]
    b = int(temp[1])
    if a in person:
        number[a] += 1
        person[a] = max(person[a],b)
    else:
        person[a] = b
        number[a] = 1
maxx = -math.inf
winner = ''
sort_person = list(person.keys())
sort_person.sort()
for x in sort_person:
    if person[x] > maxx:
        maxx = person[x]
        winner = x
for j in sort_person:
    if number[j] == 1:
        print(f'{j} bid at the price of {person[j]:.1f} baht in {number[j]} time.')
    else:
        print(f'{j} bid at the price of {person[j]:.1f} baht in {number[j]} times.')
print(f'The winner is {winner}.')