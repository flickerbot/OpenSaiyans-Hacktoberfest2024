marks = []
for i in range(1, 6):
    mark = float(input(f"Enter the mark for subject {i}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Average mark: ",average)
print("Grade: ",grade)
