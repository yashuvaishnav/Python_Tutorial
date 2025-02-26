#!/usr/bin/env python3
import sys
import time
from blessed import Terminal

# -------------------------------------------------------------------------
# 1) Task Classes (demonstrating inheritance)
# -------------------------------------------------------------------------
class Task:
    """A simple Task class with an ID, title, and completion status."""
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def toggle_completion(self):
        """Toggle the completion status of the task."""
        self.completed = not self.completed

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title}"

class HighPriorityTask(Task):
    """
    A specialized Task that adds a 'priority' attribute.
    Demonstrates inheritance from the base Task class.
    """
    def __init__(self, task_id, title, priority):
        super().__init__(task_id, title)
        self.priority = priority

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title} (Priority: {self.priority})"

# -------------------------------------------------------------------------
# 2) ToDoList Class
# -------------------------------------------------------------------------
class ToDoList:
    """Manages a collection (list) of Task objects."""
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority=None):
        new_id = len(self.tasks) + 1
        if priority:
            task = HighPriorityTask(new_id, title, priority)
        else:
            task = Task(new_id, title)
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def edit_task(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title

    def toggle_completion(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle_completion()

# -------------------------------------------------------------------------
# 3) Blessed To-Do App
# -------------------------------------------------------------------------
def main():
    term = Terminal()
    todo = ToDoList()

    # UI state variables
    mode = 'normal'  # Modes: normal, input_title, input_title_high, input_priority, edit
    title_input = ""
    priority_input = ""
    high_title = ""   # To store the title for a high-priority task
    selected_index = 0

    instructions = (
        "Commands: n = add normal, h = add high, e = edit, t = toggle, d = delete, "
        "↑/↓ = move, q = quit"
    )

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.clear)
        while True:
            # Instead of clearing completely, move the cursor home.
            print(term.home)
            # Header
            header = term.bold_blue("Blessed To-Do App")
            print(header)
            # Instructions
            print(term.yellow(instructions))
            # Show current mode and input (if any)
            if mode in ('input_title', 'input_title_high', 'edit'):
                prompt = "Enter Task Title: " if mode != 'edit' else "Edit Task Title: "
                print(prompt + title_input)
            elif mode == 'input_priority':
                print("Enter Priority (default 'High'): " + priority_input)
            else:
                print(" " * term.width)  # blank line in normal mode

            # Display the task list starting at a fixed row
            print(term.underline("Tasks:"))
            y = 0
            if todo.tasks:
                for idx, task in enumerate(todo.tasks):
                    if idx == selected_index:
                        line = term.reverse + f"{idx+1}. {task}" + term.normal
                    else:
                        line = f"{idx+1}. {task}"
                    print(line)
                    y += 1
            else:
                print("No tasks yet.")
            # Footer: display current mode info
            print(term.bold("Mode: " + mode))
            sys.stdout.flush()

            # Get a key press (with timeout)
            key = term.inkey(timeout=0.5)
            if not key:
                continue

            # Quit?
            if key.lower() == 'q':
                break

            # Process keys based on mode
            if mode == 'normal':
                if key == 'n':
                    mode = 'input_title'
                    title_input = ""
                elif key == 'h':
                    mode = 'input_title_high'
                    title_input = ""
                elif key == 'e':
                    if todo.tasks:
                        mode = 'edit'
                        title_input = todo.tasks[selected_index].title
                elif key == 't':
                    if todo.tasks:
                        todo.toggle_completion(selected_index)
                elif key == 'd':
                    if todo.tasks:
                        todo.delete_task(selected_index)
                        if selected_index >= len(todo.tasks):
                            selected_index = max(0, len(todo.tasks) - 1)
                elif key.code == term.KEY_DOWN:
                    if selected_index < len(todo.tasks) - 1:
                        selected_index += 1
                elif key.code == term.KEY_UP:
                    if selected_index > 0:
                        selected_index -= 1
            elif mode in ('input_title', 'input_title_high', 'edit'):
                if key.code in (term.KEY_ENTER,):
                    if title_input.strip():
                        if mode == 'input_title':
                            todo.add_task(title_input.strip())
                            mode = 'normal'
                        elif mode == 'input_title_high':
                            # Save the title and switch to priority input mode.
                            high_title = title_input.strip()
                            mode = 'input_priority'
                        elif mode == 'edit':
                            todo.edit_task(selected_index, title_input.strip())
                            mode = 'normal'
                    title_input = ""
                elif key.code in (term.KEY_BACKSPACE, term.KEY_DELETE):
                    title_input = title_input[:-1]
                else:
                    title_input += key
            elif mode == 'input_priority':
                if key.code in (term.KEY_ENTER,):
                    # Add a high-priority task using high_title and current priority input.
                    if high_title:
                        todo.add_task(high_title, priority=priority_input.strip() or "High")
                    mode = 'normal'
                    high_title = ""
                    priority_input = ""
                elif key.code in (term.KEY_BACKSPACE, term.KEY_DELETE):
                    priority_input = priority_input[:-1]
                else:
                    priority_input += key

            # Instead of clearing completely each time (which can blink),
            # we simply use home to rewrite the screen.
            # A short sleep can help smooth out the updates.
            time.sleep(0.05)
        print(term.clear)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
