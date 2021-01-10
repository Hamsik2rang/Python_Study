student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = -1
for score in student_scores:
    if max < score:
        max = score

print(f"The highest score in the class is: {max}")
