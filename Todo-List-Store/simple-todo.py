
def disply_query():
  print(".............................")
  print("1 view todo list")
  print("2 add todo")
  print("3 edit todo")
  print("4 delete todo")
  print("5 Exit from todo app.")
  
def view_todo_list(tasks):
  if not tasks:
    print("Todo list is empty!")
  else:
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")
  
def add_todo(tasks):
  todo = input("Enter todo: ")
  tasks.append(todo)
  print(f"{todo} added successfully!")

def edit_todo(tasks):
  view_todo_list(tasks)
  change_todo_in_list = int(input("Change your choice to edit todo: "))-1
  if change_todo_in_list >= 0 and len(tasks) >= change_todo_in_list:
    new_todo = input("Enter updated todo: ")
    tasks[change_todo_in_list] = new_todo
    print(f"{tasks[change_todo_in_list]} updated successfully!")
  else:
    print("Invalid choice!")
  
def delete_todo(tasks):
  delete_todo_in_list = int(input("Enter which todo want to delete: "))-1
  if delete_todo_in_list >= 0 and len(tasks) >= delete_todo_in_list:
    tasks.pop(delete_todo_in_list)
    print("todo is deleted succesfully")
  else:
    print("Invalid choice!")

def main():
  tasks = []
  while True:
    disply_query()
    choice = int(input("Enter your choice (1-5): "))
    if (choice == 1):
      view_todo_list(tasks)
    elif (choice == 2):
      add_todo(tasks)
    elif (choice == 3):
      edit_todo(tasks)
    elif (choice == 4):
      delete_todo(tasks)
    elif (choice == 5):
      print("Thank you for participating. Goodbye!")
      break
    else:
      print("Invalid choice! Please try between (1-5).")


if __name__ == "__main__":
  main()