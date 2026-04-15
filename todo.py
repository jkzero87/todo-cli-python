import sys              # Permite terminar el programa y trabajar con el sistema
import json             # Permite leer/escribir datos en formato JSON
import os               # Permite verificar si archivos existen
import argparse         # Permite crear CLI profesional (manejo de argumentos)

# =============================
# CONFIGURACIÓN DEL CLI
# =============================

# Creamos el parser principal (el que interpreta los comandos)
parser = argparse.ArgumentParser(description="Todo CLI")

# Creamos subcomandos: add, list, done, delete
subparsers = parser.add_subparsers(dest="command")

# -------- COMANDO ADD --------
add_parser = subparsers.add_parser("add")
add_parser.add_argument("task", help="Tarea a agregar")
# Esto significa:
# python3 todo.py add "algo"
# args.task = "algo"

# -------- COMANDO LIST --------
subparsers.add_parser("list")
# No necesita argumentos

# -------- COMANDO DONE --------
done_parser = subparsers.add_parser("done")
done_parser.add_argument("index", type=int)
# Ejemplo:
# python3 todo.py done 1
# args.index = 1

# -------- COMANDO DELETE --------
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("index", type=int)


# =============================
# FUNCIONES (LÓGICA DEL PROGRAMA)
# =============================

def handle_add(task_text, tasks, FILE):
    """
    Agrega una nueva tarea a la lista y la guarda en el archivo
    """
    tasks.append({
        "task": task_text,
        "done": False
    })

    # Guardar en archivo
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print("Tarea agregada")


def handle_list(tasks):
    """
    Muestra todas las tareas en pantalla
    """
    if not tasks:
        print("No hay tareas")
    else:
        for i, task in enumerate(tasks, start=1):
            # Si está completada → ✓, si no → ✗
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")


def handle_done(index, tasks, FILE):
    """
    Marca una tarea como completada
    """
    index = index - 1  # Convertimos de base 1 a base 0

    # Validación para evitar errores
    if index < 0 or index >= len(tasks):
        print("tarea no válida")
        sys.exit(1)

    # Cambiamos el estado de la tarea
    tasks[index]["done"] = True

    # Guardamos cambios
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print("Tarea marcada como completada")


def handle_delete(index, tasks, FILE):
    """
    Elimina una tarea de la lista
    """
    index = index - 1  # Convertimos índice

    if index < 0 or index >= len(tasks):
        print("tarea no válida")
        sys.exit(1)

    # Eliminamos la tarea
    tasks.pop(index)

    # Guardamos cambios
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print("Tarea eliminada")


# =============================
# MANEJO DE DATOS (ARCHIVO)
# =============================

FILE = "tasks.json"

# Si el archivo existe → lo leemos
if os.path.exists(FILE):
    try:
        with open(FILE, "r") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        # Si el archivo está vacío o corrupto
        tasks = []
else:
    # Si no existe, empezamos con lista vacía
    tasks = []


# =============================
# EJECUCIÓN DEL PROGRAMA
# =============================

# Parseamos los argumentos del usuario
args = parser.parse_args()

# Extraemos el comando (add, list, etc.)
command = args.command

# Si no se escribe comando → mostrar ayuda
if command is None:
    parser.print_help()
    sys.exit(1)


# =============================
# CONTROL DE FLUJO
# =============================

# Aquí conectamos los comandos con las funciones

if command == "add":
    handle_add(args.task, tasks, FILE)

elif command == "list":
    handle_list(tasks)

elif command == "done":
    handle_done(args.index, tasks, FILE)

elif command == "delete":
    handle_delete(args.index, tasks, FILE)