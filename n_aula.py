"""
Improve: if someone puts add in prompt, it shall be treated.
"""
import os

while True:
    redo_stock = None
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
        redo_stock = []
        for i in past_commands:
            if 'undo' in i:
                redo_stock.append(i)
            elif 'add' in i:
                redo_stock = []
        if redo_stock != []:
            redone_task = past_commands.pop(-1)
            task_list.append(redone_task[5:])
            log.close
            task.close()
            log = open('log.txt', 'w+', encoding='utf8')
            task = open('task.txt', 'w+', encoding='utf8')
            log.writelines(
                past_commands
            )
            task.writelines(
                task_list
            )
        else:
            print("It's not possible to redo.")

    elif command == 'show':
        print("\nTASKS:\n")
        for item in task.readlines():
            print(f'{item}', end='')

    elif command == 'exit':
        break
    
    else:
        redo_stock = []
        task.write(f'{command}\n')
        log.write(f'add {command}\n')
    print("\nFIM DO LOOP")
    #os.system('cls')
    print(redo_stock)
    print(past_commands)
log.close()
task.close()