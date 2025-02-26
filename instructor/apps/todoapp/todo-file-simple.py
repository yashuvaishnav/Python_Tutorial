
TASKS_FILE = "todos.txt"

class Task:
    """A simple Task class."""
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def toggle_completion(self):
        """Toggle the completion status of the task."""
        self.completed = not self.completed

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"ID: {self.id} | [{status}] {self.title}"


class HighPriorityTask(Task):
    """
    A specialized Task with a priority attribute.
    Demonstrates inheritance from the base Task class.
    """
    def __init__(self, task_id, title, priority):
        super().__init__(task_id, title)  # Initialize the parent (Task) attributes
        self.priority = priority

    def __str__(self):
        """
        Override the string representation to include priority.
        """
        status = "✔" if self.completed else "✘"
        return f"ID: {self.id} | [{status}] {self.title} (Priority: {self.priority})"



class ToDoList:
    """A class to manage and store tasks in a list using simple file I/O."""

    def __init__(self):
        self.tasks = []
        self.load_tasks()  # Load tasks from the file on startup

    def save_tasks(self):
        """Saves the tasks to a file in a simple text format."""
        with open(TASKS_FILE, "w") as file:
            for task in self.tasks:
                if isinstance(task, HighPriorityTask):
                    file.write(f"{task.id}|{task.title}|{task.completed}|{task.priority}\n")
                else:
                    file.write(f"{task.id}|{task.title}|{task.completed}\n")

    def load_tasks(self):
        """Loads tasks from a file."""
        try:
            with open(TASKS_FILE, "r") as file:
                self.tasks = []
                for line in file:
                    parts = line.strip().split("|")
                    task_id = int(parts[0])
                    title = parts[1]
                    completed = parts[2] == "True"
                    
                    if len(parts) == 4:  # If priority is present
                        priority = parts[3]
                        task = HighPriorityTask(task_id, title, priority)
                    else:
                        task = Task(task_id, title)
                    
                    task.completed = completed
                    self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []

    def view_tasks(self):
        """Displays the list of tasks."""
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for task in self.tasks:
                print(task)

    def add_task(self, title, high_priority=False):
        """Adds a task and saves to file."""
        new_id = len(self.tasks) + 1
        if high_priority:
            priority = input("Enter the priority (e.g. High, Medium, Low): ")
            new_task = HighPriorityTask(new_id, title, priority)
        else:
            new_task = Task(new_id, title)

        self.tasks.append(new_task)
        self.save_tasks()  # Save after adding
        print(f"Task '{title}' added successfully!")

    def edit_task(self):
        """Edits the title of an existing task and saves to file."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to edit: "))
                for task in self.tasks:
                    if task.id == task_id:
                        new_title = input("Enter the updated title: ")
                        task.title = new_title
                        self.save_tasks()  # Save after editing
                        print("Task updated successfully!")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")

    def delete_task(self):
        """Deletes a task and saves to file."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to delete: "))
                for task in self.tasks:
                    if task.id == task_id:
                        self.tasks.remove(task)
                        self.save_tasks()  # Save after deletion
                        print("Task deleted successfully!")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")

    def toggle_task_completion(self):
        """Toggles the completion status of a task and saves to file."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to toggle completion: "))
                for task in self.tasks:
                    if task.id == task_id:
                        task.toggle_completion()
                        self.save_tasks()  # Save after toggling completion
                        status = "completed" if task.completed else "not completed"
                        print(f"Task '{task.title}' is now {status}.")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")



def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Normal Task")
    print("3. Add High-Priority Task")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Toggle Task Completion")
    print("7. Exit")
    print("------------------------")

def main():
    todo_list = ToDoList()  # Loads tasks from file on startup

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            title = input("Enter the task title: ")
            todo_list.add_task(title, high_priority=False)
        elif choice == "3":
            title = input("Enter the task title: ")
            todo_list.add_task(title, high_priority=True)
        elif choice == "4":
            todo_list.edit_task()
        elif choice == "5":
            todo_list.delete_task()
        elif choice == "6":
            todo_list.toggle_task_completion()
        elif choice == "7":
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
