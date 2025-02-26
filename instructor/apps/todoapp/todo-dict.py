# A simple terminal-based To-Do app with dictionaries
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Toggle Task Completion")
    print("6. Exit")
    print("------------------------")


def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for task in tasks:
            status = "✔" if task['completed'] else "✘"
            print(f"ID: {task['id']} | [{status}] {task['title']}")


def add_task(tasks):
    title = input("Enter the task title: ")
    new_task = {
        "id": len(tasks) + 1,  # Auto-increment ID
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    print(f"Task '{title}' added successfully!")


def edit_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("Enter the task ID to edit: "))
            for task in tasks:
                if task['id'] == task_id:
                    new_title = input("Enter the updated title: ")
                    task['title'] = new_title
                    print("Task updated successfully!")
                    return
            print("Task ID not found!")
        except ValueError:
            print("Please enter a valid number!")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("Enter the task ID to delete: "))
            for task in tasks:
                if task['id'] == task_id:
                    tasks.remove(task)
                    print("Task deleted successfully!")
                    return
            print("Task ID not found!")
        except ValueError:
            print("Please enter a valid number!")


def toggle_task_completion(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("Enter the task ID to toggle completion: "))
            for task in tasks:
                if task['id'] == task_id:
                    task['completed'] = not task['completed']
                    status = "completed" if task['completed'] else "not completed"
                    print(f"Task '{task['title']}' is now {status}.")
                    return
            print("Task ID not found!")
        except ValueError:
            print("Please enter a valid number!")


def main():
    tasks = []  # List of dictionaries to store tasks
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            toggle_task_completion(tasks)
        elif choice == "6":
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
