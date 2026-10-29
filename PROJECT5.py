
marks = [75, 35, 60]
attendance = [90, 65, 80]
lab_scores = [80, 40, 55]

for i in range(len(marks)):
    print("Student", i + 1)

    if marks[i] < 40 or attendance[i] < 75 or lab_scores[i] < 40:
        print("High Academic Risk")
    elif marks[i] < 50 or lab_scores[i] < 50:
        print("Medium Academic Risk")
    else:
        print("Low Academic Risk")
