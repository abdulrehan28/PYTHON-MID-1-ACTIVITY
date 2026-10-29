ids = [101, 102, 103, 101, 104]
amounts = [500, 200, 300, 500, 600]

for i in range(len(ids)):
    if ids.count(ids[i]) > 1:
        print("Duplicate transaction:", ids[i])

    if amounts[i] > 500:
        print("High amount transaction:", ids[i])