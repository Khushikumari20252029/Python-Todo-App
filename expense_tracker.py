expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([item, amount])

        print("Expense Added Successfully!")

    elif choice == "2":
        print("\n===== EXPENSE LIST =====")

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense[0]} - Rs.{expense[1]}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense[1]

        print("Total Expenses = Rs.", total)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

