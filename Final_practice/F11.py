target = input().strip()
guess = input().strip()
digit = 0
new_target = []
new_guess = []

for i in range(min(len(target),len(guess))):
    if guess[i] == target[i]:
        digit += 1
    else:
        new_target.append(target[i])
        new_guess.append(guess[i])

count = 0
for ng in new_guess:
    if ng in new_target :
        count += 1
        new_target.remove(ng)
print(f'{digit}-{count}')


