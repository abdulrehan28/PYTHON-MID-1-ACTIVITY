apartments = [100, 250, 400]

for units in apartments:
    if units <= 100:
        bill = units * 2
    elif units <= 300:
        bill = 100 * 2 + (units - 100) * 4
    else:
        bill = 100 * 2 + 200 * 4 + (units - 300) * 6

    bill = bill + 50

    print("Units:", units)
    print("Bill:", bill)
    print()

apartments.sort(reverse=True)
print("Consumption ranking:", apartments)