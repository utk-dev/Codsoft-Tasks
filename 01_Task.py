# To-do List

my_tasks = []

while True:

    print("\n====== TO-DO LIST ======")
    print("1.Add a Task")
    print("2.Show All Tasks")
    print("3.Remove a Task")
    print("4.Quit")

    your_choice = input("\nWhat do you want to do? ")

    if your_choice == "1":
        new_task = input("Enter your task: ")
        my_tasks.append(new_task)
        print("Task added successfully👍")

    elif your_choice == "2":
        if len(my_tasks) == 0:
            print("Your task list is empty.")
        else:
            print("\nYour Tasks:\n")
            for index, i in enumerate(my_tasks, start=1):
                print(f"{index}.{i}")

    elif your_choice == "3":
        if len(my_tasks) == 0:
            print("No tasks available to remove.")
        else:
            print("\nCurrent Tasks:\n")
            for index, item in enumerate(my_tasks, start=1):
                print(f"{index}. {item}")
            remove_task = int(input("\nEnter task number to remove: "))
            
            if remove_task >= 1 and remove_task <= len(my_tasks):
                deleted = my_tasks.pop(remove_task - 1)
                print(f"'{deleted}' has been removed.")
            else:
                print("Invalid task number.")

    elif your_choice == "4":
        print("Closing To-Do List👋")
        break

    else:
        print("Please enter a valid option.")
