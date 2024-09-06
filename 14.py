marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(4)]
avg = sum(marks) / 4
if avg >= 75:
    grade = 'A'
elif avg >= 60:
    grade = 'B'
elif avg >= 40:
    grade = 'C'
else:
    grade = 'D'
print(f"Average: {avg}, Grade: {grade}")
