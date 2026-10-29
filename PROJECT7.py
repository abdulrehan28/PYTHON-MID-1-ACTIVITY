marks = [28, 35, 45, 60]
moderation = 5
maximum = 100

for mark in marks:
    new_mark = mark + moderation

    if new_mark > maximum:
        new_mark = maximum

    print("Original marks:", mark)
    print("Moderated marks:", new_mark)

    if new_mark >= 40:
        print("Pass")
    else:
        print("Fail")