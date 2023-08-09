scores = []

num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_subjects):
    score = float(input(f"Enter the score for subject {i+1}: "))
    scores.append(score)

average_score = sum(scores) / num_subjects

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(average_score)
print(f"\nAverage score: {average_score:.2f}")
print(f"Letter grade: {grade}")
