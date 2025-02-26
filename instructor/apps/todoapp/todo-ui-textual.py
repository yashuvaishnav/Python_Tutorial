from textual.app import App, on
from textual.containers import Grid, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import (
    Button,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    Static,
)
from textual.reactive import var

# -------------------------------------------------------------------------
# 1) Model Classes
# -------------------------------------------------------------------------
class Task:
    def __init__(self, task_id: int, title: str):
        self.id = task_id
        self.title = title
        self.completed = False

    def toggle(self) -> None:
        self.completed = not self.completed

    def __str__(self) -> str:
        return f"{'✔' if self.completed else '✘'} {self.title}"

class HighPriorityTask(Task):
    def __init__(self, task_id: int, title: str, priority: str):
        super().__init__(task_id, title)
        self.priority = priority

    def __str__(self) -> str:
        return f"{'✔' if self.completed else '✘'} {self.title} (Priority: {self.priority})"

class ToDoList:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, title: str, priority: str = None) -> None:
        new_id = len(self.tasks) + 1
        if priority:
            task = HighPriorityTask(new_id, title, priority)
        else:
            task = Task(new_id, title)
        self.tasks.append(task)

    def delete_task(self, task_id: int) -> None:
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def edit_task(self, task_id: int, new_title: str) -> None:
        for t in self.tasks:
            if t.id == task_id:
                t.title = new_title
                break

    def toggle_task(self, task_id: int) -> None:
        for t in self.tasks:
            if t.id == task_id:
                t.toggle()
                break

    def clear_tasks(self) -> None:
        self.tasks = []


# -------------------------------------------------------------------------
# 2) Main Application
# -------------------------------------------------------------------------
class ToDoApp(App):
    CSS = """
    # ... (Your CSS)
    """
    BINDINGS = [("q", "quit", "Quit")]
    selected_task_id = var(None)

    def __init__(self):
        super().__init__()
        self.todo = ToDoList()

    def compose(self):
        yield Header("OO To-Do App", id="header")
        tasks_table = DataTable(classes="tasks-table")
        tasks_table.add_columns("ID", "Title", "Priority", "Status")
        tasks_table.cursor_type = "row"
        tasks_table.zebra_stripes = True
        tasks_table.focus()  # Initially focus on the table
        buttons_panel = Vertical(
            Button("Add", variant="success", id="add"),
            Button("Edit", variant="primary", id="edit"),
            Button("Toggle", variant="warning", id="toggle"),
            Button("Delete", variant="error", id="delete"),
            Button("Clear All", variant="error", id="clear_all"),
            classes="buttons-panel"
        )
        yield Horizontal(tasks_table, buttons_panel)
        yield Footer()

    def on_mount(self):
        self.title = "OO To-Do App"
        self.sub_title = "An Object-Oriented To-Do List built with Textual"
        self._load_tasks()

    def _load_tasks(self):
        dt = self.query_one(DataTable)
        dt.clear()
        for task in self.todo.tasks:
            status = "✔" if task.completed else "✘"
            priority = getattr(task, "priority", "")
            dt.add_row(str(task.id), task.title, priority, status, key=str(task.id))

    @on(DataTable.RowSelected)
    def on_row_selected(self, event: DataTable.RowSelected):
        row_key = event.row_key
        if row_key:
            try:
                self.selected_task_id = int(row_key.value)
            except ValueError:
                self.selected_task_id = None
                print(f"Invalid row key: {row_key.value}")
        else:
            self.selected_task_id = None


    @on(Button.Pressed, "#add")
    def add_task(self, event: Button.Pressed):
        def callback(result):
            if result:
                title, priority = result
                self.todo.add_task(title, priority)
                self._load_tasks()

        self.push_screen(InputDialog("Add Task", "Task Title:", "Priority (Optional):"), callback)

    @on(Button.Pressed, "#edit")
    def edit_task(self, event: Button.Pressed):
        if self.selected_task_id is None:
            return

        current_title = next((task.title for task in self.todo.tasks if task.id == self.selected_task_id), None)
        if current_title is None:
            return

        def callback(result):
            if result:
                new_title, _ = result
                self.todo.edit_task(self.selected_task_id, new_title)
                self._load_tasks()

        dialog = InputDialog("Edit Task", "New Title:", "")
        dialog.set_initial_values(current_title, "")
        self.push_screen(dialog, callback)


    @on(Button.Pressed, "#toggle")
    def toggle_task(self, event: Button.Pressed):
        if self.selected_task_id is None:
            return
        self.todo.toggle_task(self.selected_task_id)
        self._load_tasks()

    @on(Button.Pressed, "#delete")
    def delete_task(self, event: Button.Pressed):
        if self.selected_task_id is None:
            return

        task_title = next((task.title for task in self.todo.tasks if task.id == self.selected_task_id), None)
        if task_title is None:
            return

        def check_answer(accepted):  # Callback for the QuestionDialog
            if accepted:
                self.todo.delete_task(self.selected_task_id)
                self._load_tasks()

        self.push_screen(QuestionDialog(f"Delete task '{task_title}'?"), check_answer) # Correct usage.
    @on(Button.Pressed, "#clear_all")
    def clear_all_tasks(self, event: Button.Pressed):
        def check_answer(accepted):
            if accepted:
                self.todo.clear_tasks()
                self._load_tasks()

        self.push_screen(QuestionDialog("Clear all tasks?"), check_answer)

    async def on_key(self, event) -> None:
        if event.key.lower() == "q":
            await self.action_quit()



# -------------------------------------------------------------------------
# 3) Dialog Screens
# -------------------------------------------------------------------------
class QuestionDialog(Screen):
    def __init__(self, dialog_title, initial_values=None, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Pass kwargs to the superclass
        self.dialog_title = dialog_title
        self.message = dialog_title
        self.initial_values = initial_values or ("", "")

    def compose(self):
        no_button = Button("No", variant="primary", id="no")
        no_button.focus()
        yield Grid(
            Label(self.message, id="question"),
            Button("Yes", variant="error", id="yes"),
            no_button,
            id="question-dialog",
        )

    def on_button_pressed(self, event):
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)

class InputDialog(Screen):
    def __init__(self, dialog_title, label1, label2="", *args, **kwargs): # label2 is optional
        super().__init__(*args, **kwargs)
        self.dialog_title = dialog_title
        self.label1 = label1
        self.label2 = label2
        self.input1 = None
        self.input2 = None

    def compose(self):
        yield Grid(
            Label(self.dialog_title, id="dialog-title"),
            Label(self.label1, classes="label"),
            Input(placeholder=self.label1, classes="input", id="input1"),
            Label(self.label2, classes="label"),
            Input(placeholder=self.label2, classes="input", id="input2") ,
            Static(),
            Button("Cancel", variant="warning", id="cancel"),
            Button("Ok", variant="success", id="ok"),
            id="input-dialog",
        )

    def on_mount(self):
        self.input1 = self.query_one("#input1", Input)
        self.input2 = self.query_one("#input2", Input)

    def set_initial_values(self, value1, value2=""): # value2 is optional
        if self.input1:
            self.input1.value = value1
        if self.input2 and self.label2: # Only set if label2 exists
            self.input2.value = value2

    def on_button_pressed(self, event):
        if event.button.id == "ok":
            input1 = self.input1.value if self.input1 else ""
            input2 = self.input2.value if self.input2 and self.label2 else ""
            self.dismiss((input1, input2))
        else:
            self.dismiss(())


if __name__ == "__main__":
    ToDoApp().run()
