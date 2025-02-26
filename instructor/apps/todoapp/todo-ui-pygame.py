import pygame
import sys

# -------------------------------------------------
#  1) Task Classes (Inheritance Demo)
# -------------------------------------------------
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


# -------------------------------------------------
#  2) ToDoList Class
# -------------------------------------------------
class ToDoList:
    """
    Manages a collection (list) of Task objects.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority=None):
        """
        Create and add a Task (normal or high-priority).
        If 'priority' is provided, a HighPriorityTask is created.
        """
        new_id = len(self.tasks) + 1
        if priority:
            task = HighPriorityTask(new_id, title, priority)
        else:
            task = Task(new_id, title)
        self.tasks.append(task)

    def delete_task(self, index):
        """Delete a task by its index in the list."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def edit_task(self, index, new_title):
        """Edit the title of an existing task."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title

    def toggle_completion(self, index):
        """Toggle completion for a task by index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle_completion()


# -------------------------------------------------
#  3) PyGame-based UI
# -------------------------------------------------
class ToDoApp:
    """
    A simple PyGame "UI" to display and interact with a ToDoList.
    Press keys to add, toggle, edit, and delete tasks.
    """
    def __init__(self):
        pygame.init()
        self.screen_width = 640
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PyGame To-Do List")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.small_font = pygame.font.SysFont("Arial", 20)

        self.todo_list = ToDoList()

        # State variables
        self.selected_index = 0  # Which task is "selected"
        self.input_mode = None   # "normal", "high", "edit", or None
        self.input_text = ""     # Buffer for typing titles

        # Spacing / Layout
        self.margin = 20                # Outer margin
        self.line_spacing_instructions = 25
        self.line_spacing_tasks = 30

        # Instructions
        self.instructions = [
            "Keyboard Shortcuts:",
            " Arrows Up/Down: select task",
            " N: Add normal task",
            " H: Add high-priority task",
            " T: Toggle completion",
            " E: Edit selected task",
            " D: Delete selected task",
            " Enter: confirm text input",
            " ESC: exit or cancel input",
        ]

    def run(self):
        """Main loop."""
        running = True
        while running:
            self.clock.tick(30)  # Limit to 30 FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    running = self.handle_keydown(event.key)

            self.draw()
        pygame.quit()
        sys.exit()

    # ------------------------------------
    #   3.1 Handle Keyboard Input
    # ------------------------------------
    def handle_keydown(self, key):
        """
        Handle key presses for both normal operation and text input modes.
        Returns False if user wants to exit, True otherwise.
        """
        if self.input_mode is None:
            # Not in text entry mode, handle main controls
            if key == pygame.K_ESCAPE:
                return False  # Quit
            elif key == pygame.K_DOWN:
                self.selected_index = min(self.selected_index + 1, len(self.todo_list.tasks) - 1)
            elif key == pygame.K_UP:
                self.selected_index = max(self.selected_index - 1, 0)
            elif key == pygame.K_n:
                # Enter normal task input mode
                self.input_mode = "normal"
                self.input_text = ""
            elif key == pygame.K_h:
                # Enter high-priority input mode
                self.input_mode = "high"
                self.input_text = ""
            elif key == pygame.K_t:
                self.todo_list.toggle_completion(self.selected_index)
            elif key == pygame.K_d:
                self.todo_list.delete_task(self.selected_index)
                # Adjust selected index if it goes out of range
                if self.selected_index >= len(self.todo_list.tasks):
                    self.selected_index = max(0, len(self.todo_list.tasks) - 1)
            elif key == pygame.K_e:
                # Enter edit mode
                if self.todo_list.tasks:
                    current_title = self.todo_list.tasks[self.selected_index].title
                    self.input_mode = "edit"
                    self.input_text = current_title
            else:
                pass
        else:
            # In some text input mode (normal, high, edit)
            if key == pygame.K_ESCAPE:
                # Cancel input
                self.input_mode = None
                self.input_text = ""
            elif key == pygame.K_RETURN:
                # Confirm input
                self.confirm_input()
            elif key == pygame.K_BACKSPACE:
                # Delete the last character
                self.input_text = self.input_text[:-1]
            else:
                # Add typed character to buffer
                char = self.get_char_from_key(key)
                if char:
                    self.input_text += char

        return True

    def confirm_input(self):
        """
        Called when user presses Enter in an input mode.
        """
        text = self.input_text.strip()
        if not text:
            self.input_mode = None
            return

        if self.input_mode == "normal":
            self.todo_list.add_task(text)
            self.selected_index = len(self.todo_list.tasks) - 1

        elif self.input_mode == "high":
            # We'll just default the priority to "High" for simplicity
            self.todo_list.add_task(text, priority="High")
            self.selected_index = len(self.todo_list.tasks) - 1

        elif self.input_mode == "edit":
            self.todo_list.edit_task(self.selected_index, text)

        # Reset input state
        self.input_mode = None
        self.input_text = ""

    def get_char_from_key(self, key):
        """
        Convert a pygame key code to a character for text entry (basic ASCII).
        """
        # For simplicity, let's allow only letters, numbers, space, some punctuation
        if pygame.K_a <= key <= pygame.K_z:
            return chr(key)
        elif pygame.K_0 <= key <= pygame.K_9:
            return chr(key)
        elif key == pygame.K_SPACE:
            return " "
        elif key in (pygame.K_MINUS, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_COLON, pygame.K_SEMICOLON):
            return chr(key)
        return ""

    # ------------------------------------
    #   3.2 Drawing / Rendering
    # ------------------------------------
    def draw(self):
        # Fill screen with dark background
        self.screen.fill((30, 30, 30))

        # 1) Draw instructions with margin/padding
        x_offset = self.margin
        y_offset = self.margin
        for line in self.instructions:
            text_surf = self.small_font.render(line, True, (200, 200, 200))
            self.screen.blit(text_surf, (x_offset, y_offset))
            y_offset += self.line_spacing_instructions

        # 2) Draw tasks
        y_offset += 10  # Extra gap between instructions and tasks
        for i, task in enumerate(self.todo_list.tasks):
            color = (255, 255, 255) if i == self.selected_index else (180, 180, 180)
            text = f"{task.id}. {str(task)}"
            text_surf = self.font.render(text, True, color)
            # Indent tasks a bit from the left
            self.screen.blit(text_surf, (x_offset + 30, y_offset + i * self.line_spacing_tasks))

        # 3) Draw input prompt at bottom if needed
        if self.input_mode is not None:
            prompt_map = {
                "normal": "Adding normal task: ",
                "high": "Adding high-priority task (priority=High): ",
                "edit": "Editing task title: ",
            }
            prompt = prompt_map.get(self.input_mode, "")
            input_text_surface = self.font.render(prompt + self.input_text, True, (255, 255, 0))

            # Position input near the bottom with some horizontal margin
            bottom_y = self.screen_height - self.margin - input_text_surface.get_height()
            self.screen.blit(input_text_surface, (x_offset, bottom_y))

        pygame.display.flip()


def main():
    app = ToDoApp()
    app.run()


if __name__ == "__main__":
    main()
