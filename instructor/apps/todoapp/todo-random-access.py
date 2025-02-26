import os

RECORD_SIZE = 62  # 4 + 1 + 50 + 1 + 5 + 1
DB_FILE = "todos.db"


def pack_task(task: dict) -> str:
    """
    Convert a task dict into a fixed-size record string of length RECORD_SIZE.
    Format: ID(4) + '|' + Title(50) + '|' + Completed(5) + '\n'
    """
    task_id = f"{task['id']:04d}"         # 4 digits, zero-padded
    title = task['title'][:50]            # truncate if longer than 50
    title = f"{title:<50}"                # left-justify in 50-char field
    completed = "True " if task['completed'] else "False"
    record_str = f"{task_id}|{title}|{completed}\n"
    return record_str


def unpack_task(record_line: str) -> dict:
    """
    Convert a 62-byte record line back into a task dict.
    """
    # Expecting something like: "0001|Buy milk                                          |False\n"
    # Slicing the string based on known positions
    task_id_str = record_line[0:4]
    title_str = record_line[5:55]
    completed_str = record_line[56:61]

    task_dict = {
        "id": int(task_id_str),
        "title": title_str.strip(),
        "completed": completed_str.strip() == "True"
    }
    return task_dict


def get_task_count():
    """
    Returns how many tasks are in the file by checking the file size.
    """
    if not os.path.exists(DB_FILE):
        return 0
    file_size = os.path.getsize(DB_FILE)
    # Each record is RECORD_SIZE bytes
    return file_size // RECORD_SIZE


def read_task_by_index(index: int) -> dict:
    """
    Read the task at given index (0-based) from the file.
    """
    with open(DB_FILE, "r") as f:
        offset = index * RECORD_SIZE
        f.seek(offset)
        record_line = f.read(RECORD_SIZE)
        if len(record_line) < RECORD_SIZE:
            # Reached EOF or invalid read
            return None
        return unpack_task(record_line)


def write_task_at_index(index: int, task: dict):
    """
    Write a task dict at the given index.
    """
    record_str = pack_task(task)
    if len(record_str) != RECORD_SIZE:
        raise ValueError("Record string is not the expected length.")
    with open(DB_FILE, "r+") as f:
        offset = index * RECORD_SIZE
        f.seek(offset)
        f.write(record_str)


def create_task(title: str, completed: bool = False):
    """
    Create a new task by appending at the end of the file.
    """
    current_count = get_task_count()
    new_id = current_count + 1  # Simple ID assignment
    task = {
        "id": new_id,
        "title": title,
        "completed": completed
    }
    record_str = pack_task(task)
    with open(DB_FILE, "a") as f:
        f.write(record_str)
    print(f"Task created with ID {new_id}")


def update_task(task_id: int, title: str = None, completed: bool = None):
    """
    Find the task by ID, update its fields, and overwrite in place.
    """
    # Task IDs are 1-based, but our file index is 0-based.
    index = task_id - 1

    existing_task = read_task_by_index(index)
    if not existing_task or existing_task["id"] != task_id:
        print("Task not found.")
        return

    if title is not None:
        existing_task["title"] = title
    if completed is not None:
        existing_task["completed"] = completed

    write_task_at_index(index, existing_task)
    print(f"Task {task_id} updated successfully.")


def delete_task(task_id: int):
    """
    Mark a task as deleted or clear it. We'll just set title to 'DELETED'.
    """
    index = task_id - 1
    existing_task = read_task_by_index(index)
    if not existing_task or existing_task["id"] != task_id:
        print("Task not found.")
        return

    # For demonstration, we set the title to "DELETED" and completed = False
    existing_task["title"] = "DELETED"
    existing_task["completed"] = False
    write_task_at_index(index, existing_task)
    print(f"Task {task_id} marked as DELETED.")


def list_all_tasks():
    """
    Print all tasks from the file. Skips over empty/invalid records.
    """
    count = get_task_count()
    for i in range(count):
        task = read_task_by_index(i)
        if task:
            status = "Done" if task["completed"] else "Not Done"
            print(f"ID: {task['id']} | Title: {task['title']} | Completed: {status}")


def main_menu():
    while True:
        print("\n--- ToDo App ---")
        print("1. List tasks")
        print("2. Create task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_all_tasks()
        elif choice == "2":
            title = input("Enter title: ")
            create_task(title, completed=False)
        elif choice == "3":
            task_id = int(input("Enter task ID to edit: "))
            new_title = input("Enter new title (leave blank to skip): ")
            if new_title.strip() == "":
                new_title = None
            new_completed_str = input("Is it completed? (y/n, leave blank to skip): ")
            new_completed = None
            if new_completed_str.lower() == "y":
                new_completed = True
            elif new_completed_str.lower() == "n":
                new_completed = False
            update_task(task_id, new_title, new_completed)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
