"""
Improve: 
    if someone puts add in prompt, it shall be treated.
Challenges:
    Isolate logic into functions.
"""
import os
import json

def add_task(list= None, input= None):
    list.append(input)
    print(f'{input} added.')

def show_task(list= None):
    if list != []:
        print("TASKS:")
        for i in list:
            print(f'\t{i}')
        return
    print("There is no task to show.")

def undo_task(list_one= None, list_two=None):
    if list_one != []:
        undone_task = list_one.pop(-1)
        list_two.append(undone_task)
        print(f'{undone_task} undone.')
        return
    print("It's not possible to execute undo.")

def redo_task(list_one=None, list_two=None):
    if list_two != []:
        redone_task = list_two.pop(-1)
        list_one.append(redone_task)
        print(f'{redone_task} redone.')
        return
    print("It's not possible to execute redo.")

def load_task(file= None):
    try:
        with open(file, 'r') as task_data:
            list_one = json.load(task_data)
        return list_one
    except FileNotFoundError:
        print("File not found!")
        
task_undone = []

tasks = load_task('task.json')

if tasks == None:
    tasks = []

while True:
    command_choice = input("Type a task to add or the following commands: show, undo, redo, exit.\n")
    commands = {
        'add' : lambda: add_task(tasks, command_choice),
        'show' : lambda: show_task(tasks),
        'undo' : lambda: undo_task(tasks, task_undone),
        'redo' : lambda: redo_task(tasks, task_undone),
    }
    if command_choice not in commands and command_choice != 'exit':
        commands.get('add')()
        continue
    elif command_choice == 'exit':
        break
    commands.get(command_choice)()

with open('task.json', 'w+') as task_data:
    json.dump(tasks, task_data)