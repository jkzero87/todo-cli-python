# Todo CLI en Python

Gestor de tareas para la terminal. Guarda las tareas en un archivo JSON y
usa `argparse` para los subcomandos. Sin dependencias externas: solo Python 3.

## Uso

```bash
python3 todo.py add "Estudiar Python"   # agrega una tarea
python3 todo.py list                    # lista todas
python3 todo.py done 1                  # marca la 1 como completada
python3 todo.py delete 1                # elimina la 1
```

Ejemplo de una sesión:

```
$ python3 todo.py add "Estudiar Python"
Tarea agregada
$ python3 todo.py add "Repasar SQL"
Tarea agregada
$ python3 todo.py done 1
Tarea marcada como completada
$ python3 todo.py list
1. [✓] Estudiar Python
2. [✗] Repasar SQL
```

Las tareas se numeran desde 1. Un número que no existe imprime
`tarea no válida` y sale con código 1. Sin subcomando, muestra la ayuda.

Las tareas viven en `tasks.json`, en la carpeta desde donde se ejecuta el
comando. El archivo se crea con la primera tarea y está en `.gitignore`. Si se
corrompe o queda vacío, el programa arranca con una lista vacía.

## Qué practiqué

- Lectura y escritura de archivos con JSON
- Subcomandos con `argparse`
- Validación de entradas
- Operaciones CRUD

## Ideas pendientes

- `undo` para desmarcar una tarea
- Colores en la terminal
- Instalarlo como comando global (`todo`)
- Guardar `tasks.json` en una ruta fija para no depender de la carpeta actual
