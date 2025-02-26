import tkinter as tk
from tkinter import messagebox, simpledialog


# -----------------------------
#    Task Classes
# -----------------------------
class Task:
    """
    A simple Task class with an ID, title, and completion status.
    """
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
    A specialized Task with a 'priority' attribute. Demonstrates inheritance.
    """
    def __init__(self, task_id, title, priority):
        super().__init__(task_id, title)
        self.priority = priority

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"ID: {self.id} | [{status}] {self.title} (Priority: {self.priority})"


# -----------------------------
#    To-Do List Class
# -----------------------------
class ToDoList:
    """
    Manages a collection (list) of tasks.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, title, high_priority=False):
        """
        Adds a normal Task or a HighPriorityTask (if high_priority=True).
        """
        new_id = len(self.tasks) + 1
        if high_priority:
            # In a GUI flow, we might ask for the priority via a popup
            # but let's handle that outside for clarity.
            pass
        else:
            new_task = Task(new_id, title)
            self.tasks.append(new_task)

    def add_high_priority_task(self, title, priority):
        """
        Creates and adds a HighPriorityTask.
        """
        new_id = len(self.tasks) + 1
        new_task = HighPriorityTask(new_id, title, priority)
        self.tasks.append(new_task)


# -----------------------------
#    Main GUI Application
# -----------------------------
class ToDoApp(tk.Tk):
    """
    The main application window for our To-Do List, using Tkinter.
    """
    def __init__(self):
        super().__init__()
        self.title("To-Do List GUI")
        self.geometry("400x300")

        # Create an instance of our ToDoList to manage tasks
        self.todo_list = ToDoList()

        # --- Create GUI Layout ---
        # 1) Listbox to display tasks
        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack(fill="both", expand=True, padx=5, pady=5)

        # 2) Frame for user input (Add Task)
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=5)

        tk.Label(entry_frame, text="Task Title:").pack(side=tk.LEFT)
        self.title_entry = tk.Entry(entry_frame)
        self.title_entry.pack(side=tk.LEFT, padx=5)

        # 3) Button frame for operations
        button_frame = tk.Frame(self)
        button_frame.pack()

        btn_add_normal = tk.Button(
            button_frame, text="Add Normal Task",
            command=self.add_normal_task
        )
        btn_add_normal.grid(row=0, column=0, padx=5, pady=5)

        btn_add_high = tk.Button(
            button_frame, text="Add High-Priority Task",
            command=self.add_high_priority_task
        )
        btn_add_high.grid(row=0, column=1, padx=5, pady=5)

        btn_edit = tk.Button(
            button_frame, text="Edit Task",
            command=self.edit_task
        )
        btn_edit.grid(row=1, column=0, padx=5, pady=5)

        btn_delete = tk.Button(
            button_frame, text="Delete Task",
            command=self.delete_task
        )
        btn_delete.grid(row=1, column=1, padx=5, pady=5)

        btn_toggle = tk.Button(
            button_frame, text="Toggle Completion",
            command=self.toggle_completion
        )
        btn_toggle.grid(row=2, column=0, padx=5, pady=5)

        btn_refresh = tk.Button(
            button_frame, text="Refresh",
            command=self.refresh_task_list
        )
        btn_refresh.grid(row=2, column=1, padx=5, pady=5)

    # --- Helper Methods ---
    def add_normal_task(self):
        """Add a normal task to the to-do list."""
        title = self.title_entry.get().strip()
        if title:
            self.todo_list.add_task(title, high_priority=False)
            self.title_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showerror("Error", "Please enter a valid task title.")

    def add_high_priority_task(self):
        """Add a high-priority task to the to-do list."""
        title = self.title_entry.get().strip()
        if title:
            priority = simpledialog.askstring("Priority", "Enter the task priority (e.g., High, Medium, Low):")
            if priority:
                self.todo_list.add_high_priority_task(title, priority)
                self.title_entry.delete(0, tk.END)
                self.refresh_task_list()
            else:
                messagebox.showerror("Error", "No priority provided.")
        else:
            messagebox.showerror("Error", "Please enter a valid task title.")

    def edit_task(self):
        """Edit the selected task's title."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            selected_task = self.todo_list.tasks[selected_index]
            new_title = simpledialog.askstring("Edit Task", "Enter new title:", initialvalue=selected_task.title)
            if new_title:
                selected_task.title = new_title
                self.refresh_task_list()

    def delete_task(self):
        """Delete the selected task."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            self.todo_list.tasks.pop(selected_index)
            self.refresh_task_list()

    def toggle_completion(self):
        """Toggle the completion status of the selected task."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            task = self.todo_list.tasks[selected_index]
            task.toggle_completion()
            self.refresh_task_list()

    def refresh_task_list(self):
        """Refresh the listbox with the latest tasks."""
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def get_selected_task_index(self):
        """
        Get the index of the currently selected task in the listbox.
        Returns None if nothing is selected.
        """
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "No task selected.")
            return None
        return selection[0]


# -----------------------------
#    Main Entry Point
# -----------------------------
def main():
    app = ToDoApp()
    app.mainloop()


if __name__ == "__main__":
    main()
