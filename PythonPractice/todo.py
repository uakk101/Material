def display_menu():
    print("\nWelcome to the To-Do List Manager!\n")
    print("1. View the to-do list")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks(tasks):
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['description']}")


def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    print("\nTask added successfully!")


def mark_task_completed(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("\nTask marked as completed!")
    else:
        print("\nInvalid task number.")


def delete_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("\nTask deleted successfully!")
    else:
        print("\nInvalid task number.")


def main():
    tasks = []

    loop = True

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            description = input("\nEnter the task description: ")
            add_task(tasks, description)
        elif choice == "3":
            task_number = int(input("\nEnter the task number to mark as completed: "))
            mark_task_completed(tasks, task_number)
        elif choice == "4":
            task_number = int(input("\nEnter the task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == "5":
            print("\nGoodbye!")
            #loop = False
            #break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
