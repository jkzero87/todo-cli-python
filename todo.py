import sys
import json
import os
import argparse

parser = argparse.ArgumentParser(description="Todo CLI")
subparsers = parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add")
add_parser.add_argument("task", help="Tarea a agregar")
subparsers.add_parser("list")
done_parser = subparsers.add_parser("done")
done_parser.add_argument("index", type=int)
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("index", type=int)


FILE = "tasks.json"

import sys
import json
import os
import argparse

parser = argparse.ArgumentParser(description="Todo CLI")
subparsers = parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add")
add_parser.add_argument("task", help="Tarea a agregar")
subparsers.add_parser("list")
done_parser = subparsers.add_parser("done")
done_parser.add_argument("index", type=int)
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("index", type=int)


FILE = "tasks.json"

if os.path.exists(FILE):
    with open(FILE , "r") as f:
        tasks = json.load(f)
else:
    tasks = []

args = parser.parse_args()

command = args.command 

if command is None:
    parser.print_help()
    sys.exit(1) 

if command == "add":
    task_text = args.task
    tasks.append({
        "task": task_text,
        "done": False
        })
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print("Tarea agregada")

elif command == "list":
    if not tasks:
        print("No hay tareas")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
            
elif command == "done":
   
    index = args.index - 1

    if index < 0 or index >= len(tasks):
        print("tarea no válida")
        sys.exit(1)

    tasks[index]["done"] = True

    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)
        
    print("Tarea marcada como completada")

elif command == "delete":
    index = args.index - 1

    if index < 0 or index >= len(tasks):
        print("tarea no válida")
        sys.exit(1)

    tasks.pop(index)

    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print("Tarea eliminada")

args = parser.parse_args()

command = args.command 

def handle_add(task_text, tasks, FILE):
    tasks.append({
        "task": task_text,
        "done": False
        })
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print("Tarea agregada")    
    

if command == "add":
    handle_add(args.task, tasks, FILE)
    
elif command == "list":
    if not tasks:
        print("No hay tareas")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
            
elif command == "done":
   
    index = args.index - 1

    if index < 0 or index >= len(tasks):
        print("tarea no válida")
        sys.exit(1)

    tasks[index]["done"] = True

    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)
        
    print("Tarea marcada como completada")

elif command == "delete":
    index = args.index - 1

    if index < 0 or index >= len(tasks):
        print("tarea no válida")
        sys.exit(1)

    tasks.pop(index)

    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print("Tarea eliminada")