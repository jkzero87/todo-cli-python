import sys
import json
import os

FILE = "Tasks.json"

if os.path.exists(FILE):
    with open(FILE , "r") as f:
        tasks = json.load(f)
else:
    tasks = []

args = sys.argv

if len(args) < 2:
    print("Uso: python3 todo.py [add|list]")
    sys.exit(1)

command = args[1]

if command == "add":
    if len(args) < 3:
        print("Debes escribir una tarea")
        sys.exit(1)
    task_text = args[2]
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
    if len(args) < 3:
        print("Debes escribir el número de la tarea")
        sys.exit()

    index = int(args[2]) - 1

    if index < 0 or index >= len(tasks):
        print("tarea no válida")
        sys.exit()

    tasks[index]["done"] = True

    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)
        
    print("Tarea marcada como completada")