# ###Proyecto: Gestor de Tareas (To-Do List)

# Crea un programa de línea de comandos para gestionar tareas pendientes, donde el usuario pueda agregar, ver, marcar como completada y eliminar tareas.
# Funcionalidades básicas:

#     Agregar tarea: El usuario ingresa una descripción de la tarea.

#     Listar tareas: Muestra todas las tareas con su estado (pendiente/completada).

#     Marcar como completada: El usuario selecciona una tarea para marcarla como completada.

#     Eliminar tarea: Elimina una tarea de la lista.

#     Salir: Cierra el programa.
import json

tareas = []


def mostrar_menu():
    print("\n----Lista de Tareas----")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Crear archivo .txt")
    print("6. Salir")


def agregar_tarea():
    tarea = input("Ingresa la descripción de la tarea: ")
    tareas.append({"descripcion": tarea, "completada": False})
    print(f"Tarea '{tarea}' agregada.")


def listar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
        return
    print("\nTareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['descripcion']} - {estado}")


def marcar_completada():
    listar_tareas()
    if not tareas:
        return
    try:
        indice = int(
            input("Selecciona el número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print(
                f"Tarea '{tareas[indice]['descripcion']}' marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def eliminar_tarea():
    listar_tareas()
    if not tareas:
        return
    try:
        indice = int(
            input("Selecciona el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(
                f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def crear_archivo():
    arch = open("lista de tareas.txt", "a")
    archivo_tareas = json.dumps([tareas], indent=4)
    arch.write(archivo_tareas)
    arch.close()

    arch = open("lista de tareas.txt", "r")
    print("\nArchivo creado")
    print(arch.read())


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        crear_archivo()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
