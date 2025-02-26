import os

# Get the absolute path of the current script's directory (todoapp)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set the "data" folder inside the "todoapp" directory
DATA_DIR = os.path.join(BASE_DIR, "data")

# Ensure the "data" folder exists
os.makedirs(DATA_DIR, exist_ok=True)

# File path for storing the tasks
FILE_NAME = os.path.join(DATA_DIR, "todo_list.txt")


# A simple terminal-based To-Do app with dictionaries and file persistence
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Toggle Task Completion")
    print("6. Exit")
    print("------------------------")


def load_tasks():
    """Load tasks from a text file into a list of dictionaries."""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    task_id, title, completed = parts
                    tasks.append({
                        "id": int(task_id),
                        "title": title,
                        "completed": completed == "True"
                    })
    return tasks


def save_tasks(tasks):
    """Save the list of tasks to a text file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['title']}|{task['completed']}\n")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for task in tasks:
            status = "✔" if task['completed'] else "✘"
            print(f"ID: {task['id']} | [{status}] {task['title']}")


def add_task(tasks):
    """Add a new task."""
    title = input("Enter the task title: ")
    new_task = {
        "id": len(tasks) + 1 if tasks else 1,  # Auto-increment ID
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")


def edit_task(tasks):
    """Edit an existing task."""
    view_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("Enter the task ID to edit: "))
            for task in tasks:
                if task['id'] == task_id:
                    new_title = input("Enter the updated title: ")
                    task['title'] = new_title
                    save_tasks(tasks)
                    print("Task updated successfully!")
                    return
            print("Task ID not found!")
        except ValueError:
            print("Please enter a valid number!")


def delete_task(tasks):
    """Delete a task by its ID."""
    view_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("Enter the task ID to delete: "))
            for task in tasks:
                if task['id'] == task_id:
                    tasks.remove(task)
                    save_tasks(tasks)
                    print("Task deleted successfully!")
                    return
            print("Task ID not found!")
        except ValueError:
            print("Please enter a valid number!")


def toggle_task_completion(tasks):
    """Toggle the completion status of a task."""
    view_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("Enter the task ID to toggle completion: "))
            for task in tasks:
                if task['id'] == task_id:
                    task['completed'] = not task['completed']
                    status = "completed" if task['completed'] else "not completed"
                    save_tasks(tasks)
                    print(f"Task '{task['title']}' is now {status}.")
                    return
            print("Task ID not found!")
        except ValueError:
            print("Please enter a valid number!")


def main():
    """Main program loop."""
    tasks = load_tasks()
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
