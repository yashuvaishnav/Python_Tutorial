import struct
import os

TASKS_FILE = "todos.dat"
NORMAL_TASK_SIZE = 55  # 4 bytes ID + 50 bytes title + 1 byte completed
HIGH_PRIORITY_TASK_SIZE = 65  # 55 bytes + 10 bytes priority


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
    """A specialized Task with priority."""
    def __init__(self, task_id, title, priority):
        super().__init__(task_id, title)
        self.priority = priority

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"ID: {self.id} | [{status}] {self.title} (Priority: {self.priority})"


class ToDoList:
    """A class to manage and store tasks in a binary file with random access."""

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def save_task(self, task, position=None):
        """Saves a task to the file at a specific position or appends it."""
        mode = "r+b" if os.path.exists(TASKS_FILE) else "wb"
        with open(TASKS_FILE, mode) as file:
            if position is not None:
                file.seek(position)  # Overwrite at specific position
            else:
                file.seek(0, os.SEEK_END)  # Append

            if isinstance(task, HighPriorityTask):
                file.write(struct.pack("I50s?10s", 
                                       task.id, 
                                       task.title.encode().ljust(50, b' '), 
                                       task.completed, 
                                       task.priority.encode().ljust(10, b' ')))
            else:
                file.write(struct.pack("I50s?", 
                                       task.id, 
                                       task.title.encode().ljust(50, b' '), 
                                       task.completed))

    def load_tasks(self):
        """Loads tasks from a binary file using random access, ensuring correct alignment."""
        if not os.path.exists(TASKS_FILE):
            return

        self.tasks = []
        with open(TASKS_FILE, "rb") as file:
            while True:
                pos = file.tell()  # Get current position
                data = file.read(NORMAL_TASK_SIZE)  # Read a full normal task record

                if not data:  # End of file
                    break  

                if len(data) == NORMAL_TASK_SIZE:  # Standard task
                    task_id, title, completed = struct.unpack("I50s?", data)
                    title = title.decode().strip()
                    task = Task(task_id, title)

                elif len(data) == HIGH_PRIORITY_TASK_SIZE:  # High-priority task
                    task_id, title, completed, priority = struct.unpack("I50s?10s", data)
                    title = title.decode().strip()
                    priority = priority.decode().strip()
                    task = HighPriorityTask(task_id, title, priority)

                else:
                    print(f"Warning: Corrupt record at position {pos}. Skipping.")
                    break  # Avoid crashing on corrupt files

                task.completed = completed
                self.tasks.append(task)


    def view_tasks(self):
        """Displays the list of tasks."""
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for task in self.tasks:
                print(task)

    def add_task(self, title, high_priority=False):
        """Adds a new task and appends it to the binary file."""
        new_id = len(self.tasks) + 1
        if high_priority:
            priority = input("Enter the priority (e.g. High, Medium, Low): ")
            new_task = HighPriorityTask(new_id, title, priority)
        else:
            new_task = Task(new_id, title)

        self.tasks.append(new_task)
        self.save_task(new_task)  # Append task to file
        print(f"Task '{title}' added successfully!")

    def edit_task(self):
        """Edits the title of an existing task using random access."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to edit: "))
                for index, task in enumerate(self.tasks):
                    if task.id == task_id:
                        new_title = input("Enter the updated title: ")
                        task.title = new_title

                        position = index * (HIGH_PRIORITY_TASK_SIZE if isinstance(task, HighPriorityTask) else NORMAL_TASK_SIZE)
                        self.save_task(task, position)  # Overwrite at position
                        print("Task updated successfully!")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")

    def delete_task(self):
        """Deletes a task by marking it as inactive (or rewriting the file)."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to delete: "))
                for index, task in enumerate(self.tasks):
                    if task.id == task_id:
                        self.tasks.remove(task)

                        # Rewrite file without the deleted task
                        with open(TASKS_FILE, "wb") as file:
                            for t in self.tasks:
                                self.save_task(t)
                        
                        print("Task deleted successfully!")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")

    def toggle_task_completion(self):
        """Toggles the completion status of a task using random access."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to toggle completion: "))
                for index, task in enumerate(self.tasks):
                    if task.id == task_id:
                        task.toggle_completion()

                        position = index * (HIGH_PRIORITY_TASK_SIZE if isinstance(task, HighPriorityTask) else NORMAL_TASK_SIZE)
                        self.save_task(task, position)  # Overwrite at position
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
