seats = [
    ["S1", "S2"],
    ["S3", "S4"]
]

registered = ["R101", "R102", "R103"]
entered = []

for i in range(len(registered)):
    reg_id = input("Enter registration ID: ")

    if reg_id in registered and reg_id not in entered:
        entered.append(reg_id)
        print("Entry allowed")
    else:
        print("Invalid or duplicate entry")

print("Total entries:", len(entered))
print("Available seats:", 4 - len(entered))