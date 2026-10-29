balance = 1000
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter amount: "))
        if amount > 0:
            balance += amount
            transactions.append("Deposit: " + str(amount))
        else:
            print("Invalid amount")

    elif choice == 2:
        amount = int(input("Enter amount: "))
        if 0 < amount <= balance:
            balance -= amount
            transactions.append("Withdraw: " + str(amount))
        else:
            print("Insufficient balance or invalid amount")

    elif choice == 3:
        print("Balance:", balance)

    elif choice == 4:
        print(transactions)

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")