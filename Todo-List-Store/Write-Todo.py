import os

TODO_FILE = "todo.txt"

def load_tasks():
  if not os.path.exists(TODO_FILE):
    return []
  with open(TODO_FILE, 'r') as file:
    return [line.strip() for line in file.readlines()]
  
def save_todos(todos):
  with open(TODO_FILE,'w') as file:
    for todo in todos:
      file.write(todo + "\n")
    
def disply_query():
  print(".............................")
  print("1 view todo list")
  print("2 add todo")
  print("3 edit todo")
  print("4 delete todo")
  print("5 Exit from todo app.")
  
def view_todo_list():
  todos = load_tasks()
  if not todos:
    print("Todo list is empty!")
  else:
    for i, todo in enumerate(todos, 1):
      print(f"{i}. {todo}")
  
def add_todo():
  todo = input("Enter todo: ")
  todos = load_tasks()
  todos.append(todo)
  save_todos(todos)
  print(f"{todo} added successfully!")
  
  
def edit_todo():
  todos = load_tasks()
  view_todo_list()
  change_todo_in_list = int(input("Change your choice to edit todo: "))-1
  if change_todo_in_list >= 0 and len(todos) >= change_todo_in_list:
    new_todo = input("Enter updated todo: ")
    todos[change_todo_in_list] = new_todo
    save_todos(todos)
    print("Todo updated successfully!")
  else:
    print("Invalid choice!")
  
def delete_todo():
  todos = load_tasks()
  view_todo_list()
  delete_todo_in_list = int(input("Enter which todo want to delete: "))-1
  if delete_todo_in_list >= 0 and len(todos) >= delete_todo_in_list:
    todos.pop(delete_todo_in_list)
    save_todos(todos)
    print("todo is deleted succesfully")
  else:
    print("Invalid choice!")


def main():
  while True:
    disply_query()
    choice = int(input("Enter your choice (1-5): "))
    if (choice == 1):
      view_todo_list()
    elif (choice == 2):
      add_todo()
    elif (choice == 3):
      edit_todo()
    elif (choice == 4):
      delete_todo()
    elif (choice == 5):
      print("Thank you for participating. Goodbye!")
      break
    else:
      print("Invalid choice! Please try between (1-5).")


if __name__ == "__main__":
  main()