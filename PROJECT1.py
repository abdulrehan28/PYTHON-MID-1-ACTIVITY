schedule = [
    ("Python", 9, 10, "Room A"),
    ("Maths", 9, 11, "Room B"),
    ("English", 11, 12, "Room C")
]

for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        c1, s1, e1, r1 = schedule[i]
        c2, s2, e2, r2 = schedule[j]

        if s1 < e2 and s2 < e1:
            print(c1, "and", c2, "have a time clash")