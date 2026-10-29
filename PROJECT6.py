rooms = [
    [101, 120, 500],
    [102, 250, 800],
    [103, 100, 400]
]

for room in rooms:
    number, electricity, water = room

    bill = electricity * 5 + water * 2

    print("Room:", number)
    print("Total bill:", bill)

    if electricity > 200 or water > 700:
        print("High consumption")

    print()