areas = [
    ["Area A", 50, 1],
    ["Area B", 30, 2],
    ["Area C", 40, 3]
]

stock = 80

areas.sort(key=lambda x: x[2])

for area in areas:
    name, demand, priority = area

    supplied = min(demand, stock)
    remaining = demand - supplied
    stock = stock - supplied

    print("Area:", name)
    print("Supplied:", supplied)
    print("Unmet demand:", remaining)

print("Remaining stock:", stock)