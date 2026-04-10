tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Clear All Tasks")
    print("6. Show Stats")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task_name = input("Enter task: ").strip()
        if task_name == "":
            print("Task cannot be empty!")
        else:
            tasks.append({"task": task_name, "completed": False})
            print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, t in enumerate(tasks):
                status = "✓" if t["completed"] else "☐"
                print(f"{i+1}. {status} {t['task']}")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark.")
        else:
            for i, t in enumerate(tasks):
                status = "✓" if t["completed"] else "☐"
                print(f"{i+1}. {status} {t['task']}")
            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]["completed"] = True
                    print("Marked as complete!")
                else:
                    print("Invalid task number!")
            except:
                print("Invalid input!")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks):
                status = "✓" if t["completed"] else "☐"
                print(f"{i+1}. {status} {t['task']}")
            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num-1)
                    print("Task deleted!")
                else:
                    print("Invalid task number!")
            except:
                print("Invalid input!")

    elif choice == "5":
        tasks.clear()
        print("All tasks cleared!")

    elif choice == "6":
        total = len(tasks)
        completed = sum(1 for t in tasks if t["completed"])
        pending = total - completed
        print(f"Total: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")