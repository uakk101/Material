import os
def display_menu():
    print("\nWelcome to the To-Do List Manager!\n")
    print("1. View the to-do list")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks():
    if not os.path.exists("todo.txt"):
        print("\nNo tasks found.")
        return

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task.startswith("x") else "[ ]"
            description = task[3:].strip()
            print(f"{i}. {status} {description}")


def add_task(description):
    with open("todo.txt", "a") as file:
        file.write(f"\n[ ] {description}")
    print("\nTask added successfully!")


def mark_task_completed(task_number):
    if not os.path.exists("todo.txt"):
        print("\nNo tasks found.")
        return

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if not tasks or task_number < 1 or task_number > len(tasks):
        print("\nInvalid task number.")
        return

    tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[x]")

    with open("todo.txt", "w") as file:
        file.writelines(tasks)

    print("\nTask marked as completed!")


def delete_task(task_number):
    if not os.path.exists("todo.txt"):
        print("\nNo tasks found.")
        return

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if not tasks or task_number < 1 or task_number > len(tasks):
        print("\nInvalid task number.")
        return

    del tasks[task_number - 1]

    with open("todo.txt", "w") as file:
        file.writelines(tasks)

    print("\nTask deleted successfully!")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            description = input("\nEnter the task description: ")
            add_task(description)
        elif choice == "3":
            task_number = int(input("\nEnter the task number to mark as completed: "))
            mark_task_completed(task_number)
        elif choice == "4":
            task_number = int(input("\nEnter the task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
