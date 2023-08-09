def calculate_average(scores):
    total_subjects = len(scores)
    total_score = sum(scores.values())
    average_score = total_score / total_subjects
    return average_score


scores = {}
num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_subjects):
    subject = input(f"Enter the name of subject {i+1}: ")
    score = float(input(f"Enter the score for subject {i+1}: "))
    scores[subject] = score
    
average_score = calculate_average(scores)

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

grade_points = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

print(f"\nAverage score: {average_score:.2f}")
print(f"Letter grade: {grade}")
print(f"Grade points: {grade_points[grade]}")
