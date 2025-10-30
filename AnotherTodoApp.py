tasks = []
answer = ""
while answer != 2 :
    answer = int(input("Choose Option "))

    if answer == 1 :
        task = input(f"Enter Your Task ")
        tasks.append(task)
    for task in tasks :
        print(task)
