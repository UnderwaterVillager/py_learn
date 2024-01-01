import os

while True:
    undo_counter = 0
    # PATH CHECK
    if os.path.exists('task.txt'):
        task = open('task.txt', 'a+', encoding='utf8')
    else:
        task = open('task.txt', 'w+', encoding='utf8')
    
    if os.path.exists('log.txt'):
        log = open('log.txt', 'a+', encoding='utf8')
    else:
        log = open('log.txt', 'w+', encoding='utf8')
    
    task.seek(0,0)
    log.seek(0,0)
    past_commands = log.readlines()
   
    command = input("Submit a task or a command(undo, redo, show, exit):\n")

    if command == 'undo':
        add_status = False
        print("undo em progresso!")
        task_list = task.readlines()        
        undo_counter = undo_counter - 1
        try:
            past_commands.append(f'undo {task_list.pop(undo_counter)}')
            log.close
            task.close            
            log = open('log.txt', 'w+', encoding='utf8')
            task = open('task.txt', 'w+', encoding='utf8')
            log.writelines(
                past_commands
            )
            task.writelines(
                task_list
            )
        except IndexError:
            print("There is no tasks to undo! Ok?")

    
    
    
    
    
    
    elif command == 'redo':
        if add_status == True:
            print("It's not possible to redo.")
        else:
            print("redo em progresso")
        







    elif command == 'show':
        add_status = False
        print("\nTASKS:\n")
        for item in task.readlines():
            print(f'{item}', end='')
    
    elif command == 'exit':
        break

    else:
        add_status = True
        redo_stock = []
        task.write(f'{command}\n')
        log.write(f'add {command}\n')
    print("\nFIM DO LOOP")
    os.system('cls')
log.close()
task.close()