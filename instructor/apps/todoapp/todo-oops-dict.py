"""
NOTES:

Explanation of Key OOP Concepts
--------------------------------------------
Classes (Task, HighPriorityTask, ToDoList)

Each class represents a concept.
- Task is the base class with basic attributes (id, title, and completed).
- HighPriorityTask inherits from Task, adding a priority attribute and an overridden __str__ method.
- ToDoList manages a collection of Task objects.

Inheritance
- HighPriorityTask uses super().__init__(...) to invoke the parent (Task) constructor, inheriting its 
  attributes and methods but also adding or overriding where needed.

Methods
- Inside the ToDoList class, we have methods like add_task, view_tasks, edit_task, delete_task, and 
  toggle_task_completion.
  
  These methods encapsulate the logic for each operation, improving clarity and reusability.

Encapsulation
- Each class handles its own internal data. For example, Task manages the task’s title and status, while 
  ToDoList manages the overall list of tasks.

By structuring your code with classes, you make it more organized, modular, and easier to maintain or 
extend (e.g., adding new task types, or storing/saving tasks in a file/database).

"""

# task.py
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


# to_do_list.py
class ToDoList:
    """A class to manage and store tasks in a list."""
    def __init__(self):
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
        """
        Adds a task. If high_priority is True,
        a HighPriorityTask is created instead of a regular Task.
        """
        new_id = len(self.tasks) + 1
        if high_priority:
            # Ask for priority only if user wants a HighPriorityTask
            priority = input("Enter the priority (e.g. High, Medium, Low): ")
            new_task = HighPriorityTask(new_id, title, priority)
        else:
            new_task = Task(new_id, title)

        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully!")

    def edit_task(self):
        """Edits the title of an existing task."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to edit: "))
                for task in self.tasks:
                    if task.id == task_id:
                        new_title = input("Enter the updated title: ")
                        task.title = new_title
                        print("Task updated successfully!")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")

    def delete_task(self):
        """Deletes a task."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to delete: "))
                for task in self.tasks:
                    if task.id == task_id:
                        self.tasks.remove(task)
                        print("Task deleted successfully!")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")

    def toggle_task_completion(self):
        """Toggles the completion status of a task."""
        self.view_tasks()
        if self.tasks:
            try:
                task_id = int(input("Enter the task ID to toggle completion: "))
                for task in self.tasks:
                    if task.id == task_id:
                        task.toggle_completion()
                        status = "completed" if task.completed else "not completed"
                        print(f"Task '{task.title}' is now {status}.")
                        return
                print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number!")


# main.py
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
    todo_list = ToDoList()

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
