tasks = []


def displaytasks():
    if not tasks:
        print("no tasks are available")
    else:
        for i,task in enumerate(tasks, start=1):
            status = "done" if task["completed"] else "not done"
            print(f"{i}.{task['task']}({status})")


def addtask(taskname):
    task = {"task": taskname, "completed": False}
    tasks.append(task)
    print(f"Task '{taskname}'added to your todo list")


def markcompleted(tasknumber):
    if 1 <= tasknumber <= len(tasks):
        tasks[tasknumber - 1]["completed"] = True
        print(f"task {tasknumber} marked as completed")
    else:
        print("wrong task number. please enter a correct task number. ")


def removetask(tasknumber):
    if 1 <= tasknumber <= len(tasks):
        removedtask = tasks.pop(tasknumber - 1)
        print(f"Task '{removedtask['task']} removed from your todo list.")
    else:
        print("wrong task number . please enter a correct task number. ")


while True:
    print("\menu")
    print("1.display task")
    print("2. adding task")
    print("3. mark as completed")
    print("4. remove task")
    print("5. exit")
    choice = input("enter the task")

    if choice == '1':
        displaytasks()
    elif choice == '2':
        taskname = input("enter your task")
        addtask(taskname)
    elif choice == '3':
        displaytasks()
        tasknumber = int(input("enter the task to mark as completed:"))
        markcompleted(tasknumber)
    elif choice == '4':
        displaytasks()
        tasknumber = int(input("enter the task to remove:"))
        removetask(tasknumber)
    elif choice == '5':
        break
    else:
        print("wrong choice. please enter correct choice")
