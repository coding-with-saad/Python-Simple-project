def task():
    task=[]
    print("Wellcome to task manager app")

    total_task=int(input("Enter how many task you wants to add"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i}=")
        task.append(task_name)

    print(f"today task are\n{task}")

    while True:
        operation=int(input("enter 1-Add\n2-Update\n3-Delete\n4-view\n5-Exit/stop/"))
        if operation==1:
            add=input("Enter Task you want to add=")
            task.append(add)
            print(f"Task{add} has been success fully added")

        elif operation==2:
            updatedval=input("enter your task you want to updated=")
            if updatedval in task:
                up=input("enter new tasks..")
                ind=task.index(updatedval)
                task[ind]=up
                print(f"Updated task{up}")

        elif operation==3:
            del_val=input("which task you want to delete=")
            if del_val in task:
                ind=task.index(del_val)
                del task[ind]
                print(f"Task {del_val} has been deleted")

        elif operation==4:
            print(f"Total tasks={task}")

        elif operation==5:
            print("Closing the program....")
            break

        else:
            print("Invalid input")


task()          