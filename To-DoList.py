import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n📜 No tasks available.")
    else:
        print("\n📋 To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{index}. {status} {task['task']}")

# Add a task
def add_task(tasks):
    task_name = input("\nEnter task: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print("✔ Task added!")

# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print("✔ Task marked as done!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Enter a valid number!")

# Remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"🗑 Removed: {removed_task['task']}")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Enter a valid number!")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📌 To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice, try again!")

if __name__ == "__main__":
    main()
import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n📜 No tasks available.")
    else:
        print("\n📋 To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{index}. {status} {task['task']}")

# Add a task
def add_task(tasks):
    task_name = input("\nEnter task: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print("✔ Task added!")

# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print("✔ Task marked as done!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Enter a valid number!")

# Remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"🗑 Removed: {removed_task['task']}")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Enter a valid number!")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📌 To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice, try again!")

if __name__ == "__main__":
    main()
