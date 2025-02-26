import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QInputDialog,
    QLabel
)

# -----------------------------------------
#  1) Task Classes
# -----------------------------------------
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
    A specialized Task with a 'priority' attribute.
    Demonstrates inheritance from the base Task class.
    """
    def __init__(self, task_id, title, priority):
        super().__init__(task_id, title)
        self.priority = priority

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"ID: {self.id} | [{status}] {self.title} (Priority: {self.priority})"


# -----------------------------------------
#  2) ToDoList Class
# -----------------------------------------
class ToDoList:
    """
    Manages a collection (list) of Task objects.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        """
        Creates a standard Task and adds it to the list.
        """
        new_id = len(self.tasks) + 1
        task = Task(new_id, title)
        self.tasks.append(task)

    def add_high_priority_task(self, title, priority):
        """
        Creates a HighPriorityTask and adds it to the list.
        """
        new_id = len(self.tasks) + 1
        task = HighPriorityTask(new_id, title, priority)
        self.tasks.append(task)


# -----------------------------------------
#  3) MainWindow (The PyQt GUI)
# -----------------------------------------
class MainWindow(QMainWindow):
    """
    The main window for the to-do application (using PyQt).
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List (PyQt)")
        self.setGeometry(100, 100, 500, 300)

        # Create a ToDoList instance to manage tasks
        self.todo_list = ToDoList()

        # Main widget (central widget for QMainWindow)
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Create a vertical layout for the main widget
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # -----------------------------------------
        #  Top label to show instructions
        # -----------------------------------------
        label = QLabel("Enter a task title, then choose Add Normal or Add High-Priority.")
        main_layout.addWidget(label)

        # -----------------------------------------
        #  Entry field for new task title
        # -----------------------------------------
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Enter task title here...")
        main_layout.addWidget(self.title_edit)

        # -----------------------------------------
        #  Buttons Layout
        # -----------------------------------------
        button_layout = QHBoxLayout()

        btn_add_normal = QPushButton("Add Normal Task")
        btn_add_normal.clicked.connect(self.add_normal_task)
        button_layout.addWidget(btn_add_normal)

        btn_add_high = QPushButton("Add High-Priority Task")
        btn_add_high.clicked.connect(self.add_high_priority_task)
        button_layout.addWidget(btn_add_high)

        main_layout.addLayout(button_layout)

        # -----------------------------------------
        #  List widget to display tasks
        # -----------------------------------------
        self.task_list_widget = QListWidget()
        main_layout.addWidget(self.task_list_widget)

        # -----------------------------------------
        #  Action Buttons
        # -----------------------------------------
        action_button_layout = QHBoxLayout()

        btn_edit = QPushButton("Edit Task")
        btn_edit.clicked.connect(self.edit_task)
        action_button_layout.addWidget(btn_edit)

        btn_delete = QPushButton("Delete Task")
        btn_delete.clicked.connect(self.delete_task)
        action_button_layout.addWidget(btn_delete)

        btn_toggle = QPushButton("Toggle Completion")
        btn_toggle.clicked.connect(self.toggle_completion)
        action_button_layout.addWidget(btn_toggle)

        btn_refresh = QPushButton("Refresh")
        btn_refresh.clicked.connect(self.refresh_list)
        action_button_layout.addWidget(btn_refresh)

        main_layout.addLayout(action_button_layout)

    # -----------------------------------------
    #  Helper Methods (Slots)
    # -----------------------------------------
    def add_normal_task(self):
        """
        Add a normal task to the to-do list using the text from self.title_edit.
        """
        title = self.title_edit.text().strip()
        if title:
            self.todo_list.add_task(title)
            self.title_edit.clear()
            self.refresh_list()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task title.")

    def add_high_priority_task(self):
        """
        Add a high-priority task. Prompts the user for the priority.
        """
        title = self.title_edit.text().strip()
        if title:
            priority, ok = QInputDialog.getText(self, "High Priority Task", "Enter priority (e.g. High, Medium, Low):")
            if ok and priority:
                self.todo_list.add_high_priority_task(title, priority)
                self.title_edit.clear()
                self.refresh_list()
            else:
                QMessageBox.warning(self, "Warning", "No priority entered.")
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task title.")

    def edit_task(self):
        """
        Edit the title of the currently selected task.
        """
        index = self.task_list_widget.currentRow()
        if index < 0:
            QMessageBox.warning(self, "Warning", "No task selected.")
            return

        selected_task = self.todo_list.tasks[index]
        new_title, ok = QInputDialog.getText(
            self, "Edit Task", "New title:", text=selected_task.title
        )
        if ok and new_title:
            selected_task.title = new_title
            self.refresh_list()

    def delete_task(self):
        """
        Delete the currently selected task.
        """
        index = self.task_list_widget.currentRow()
        if index < 0:
            QMessageBox.warning(self, "Warning", "No task selected.")
            return

        # Remove the task from the list
        self.todo_list.tasks.pop(index)
        self.refresh_list()

    def toggle_completion(self):
        """
        Toggle the completion status of the selected task.
        """
        index = self.task_list_widget.currentRow()
        if index < 0:
            QMessageBox.warning(self, "Warning", "No task selected.")
            return

        task = self.todo_list.tasks[index]
        task.toggle_completion()
        self.refresh_list()

    def refresh_list(self):
        """
        Refresh the QListWidget to display the latest tasks.
        """
        self.task_list_widget.clear()
        for task in self.todo_list.tasks:
            self.task_list_widget.addItem(str(task))


# -----------------------------------------
#  4) Entry Point
# -----------------------------------------
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
