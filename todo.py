tasks = []

while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"{removed} deleted!")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")

