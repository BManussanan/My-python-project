num_student = 10
count = 0
max = 0
while count < 10:
    score = float(input("Enter student's score : "))
    if score<0 or score>100:
        print("Score is out of range.")
    else:
        count = count+1
        if score > max:
           max = score
print(f"Maximum Score: {max:.1f}")