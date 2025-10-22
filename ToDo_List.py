from datetime import datetime


def is_valid_date(date_str):
    try:
        # Try to parse date with required format
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        # If parsing fails, it's not valid
        return False


# --- YOU NEED TO IMPLEMENT THIS FUNCTION ---
def userChoice(choice, tasks):
    # todo: Implement the logic based on the 'choice' parameter
    # 1. Add Task: get task_name, deadline, call add_task()
    # 2. Delete Task: get task_number, call delete_task()
    # 3. Display Tasks: call display_tasks()
    # 4. Exit: return "Exiting application. Goodbye!"
    # Else: print "Invalid choice!"
    if choice == 1:
        task_name = input('Enter task name:')
        deadline = input('Enter deadline (DD-MM-YYYY):')
        if is_valid_date(deadline):
            add_task(tasks, task_name, deadline)
        else:
            print('Invalid date format! Try again\n')
    elif choice == 2:
        if len(tasks) == 0:
            print('No tasks available.')
        else:
            display_tasks(tasks)
            task_number = int(input('Enter task number to delete:'))
            if task_number > len(tasks) or task_number <= 0:
                print('Invalid task number!')
            else:
                delete_task(tasks, task_number)
    elif choice == 3:
        if len(tasks) == 0:
            print('No tasks available.')
        else:
            display_tasks(tasks)
    elif choice == 4:
        return 'Exiting application. Goodbye!'
    else:
        print('Invalid choice!')


# --- END OF FUNCTION TO IMPLEMENT ---


def add_task(tasks, task_name, deadline):
    dict1 = {}
    dict1[task_name] = deadline
    tasks.append(dict1)
    print(f"Task {task_name} - {deadline} added successfully")
    # dict1.clear()


def delete_task(tasks, task_number):
    # name=list(tasks[task_number-1].keys())[0]
    tasks.pop(task_number - 1)
    print(f"Task with Task number {task_number} deleted successfully")


def display_tasks(tasks):
    print('Your Tasks:')
    for i in range(len(tasks)):
        for key, value in tasks[i].items():
            print(f"{i + 1}. {key} - Deadline: {value}")


if __name__ == "__main__":
    # # List to store tasks
    tasks = []
    print("""
Welcome to the To-Do List Application!
    """)

    while True:
        print("Choose one operation:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        value = userChoice(choice, tasks)
        if value == "Exiting application. Goodbye!":
            print(value)
            break