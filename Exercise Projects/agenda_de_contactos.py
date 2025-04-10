# Funcionalidades básicas:

#     Agregar contacto: Nombre, teléfono y correo electrónico.

#     Listar contactos: Muestra todos los contactos con sus datos.

#     Buscar contacto: Por nombre o teléfono (coincidencias parciales, ej: "Juan" encuentra "Juan Pérez").

#     Editar contacto: Modificar uno o más campos de un contacto existente.

#     Eliminar contacto: Eliminar un contacto de la lista.

#     Guardar/ cargar contactos: Persistir los datos en un archivo JSON.

#     Salir: Cerrar el programa.
import json


def menu():
    print("\n------Agenda de Contactos------")
    print("1. Agregar Contacto")
    print("2. Listar Contactos")
    print("3. Buscar Contacto")
    print("4. Editar Contacto")
    print("5. Eliminar Contacto")
    print("6. Guardar/Cargar Contacto")
    print("7. Salir del Programa")


def cargar_contactos():
    try:
        with open("contactos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


contactos = cargar_contactos()


def guardar_contactos():
    with open("contactos.json", "w") as archivo:
        archivo_contactos = json.dumps(contactos, indent=4)
        archivo.write(archivo_contactos)
    print("Archivo Guardado correctamente. ")


def agregar_contacto():
    nombre = input("Ingresa el nombre: ")
    telefono = input("Ingrese el numero de telefono: ")
    email = input("Ingrese el correo electronico: ")
    if "@" in email:
        pass
    else:
        print("\nIngrese un correo electronico valido")
        return agregar_contacto()
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    print("Contacto Creado")


def listar_contactos():
    try:
        if not contactos:
            print("No hay ningun contacto")
            return
        print("\nContactos: ")
        for i, contacto in enumerate(contactos, start=1):
            print(
                f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")
    except:
        print("Error al listar los contactos")


def buscar_contacto(lista_contactos):
    criterio = input("Ingresa el nombre o telefono del contacto: ")
    resultados = []

    for contactos in lista_contactos:
        if criterio.lower() in contactos["nombre"].lower() or criterio in contactos["telefono"]:
            resultados.append(contactos)

    if not resultados:
        print("No se encontraron contactos que coincidan con la busqueda.")
    else:
        print(f"\nSe encontraron {len(resultados)} contactos: ")
        for i, contactos in enumerate(resultados, start=1):
            print(
                f"{i}. {contactos['nombre']} - {contactos['telefono']} - {contactos['email']}")

    return resultados


def editar_contacto():
    listar_contactos()

    indice = int(input("Coloque el indice del contacto a editar: ")) - 1
    if 0 <= indice < len(contactos):
        print("\n Que campo quieres editar: ")
        print("1. Nombre")
        print("2. Telefono")
        print("3. email")
        print("4. Todos los campos")
        campo = input("\nOpcion:")
        if campo == "1":
            new_nombre = input("Introduce el nuevo nombre: ")
            contactos[indice]["nombre"] = new_nombre
            print("\nNombre actualizado.")
        elif campo == "2":
            new_telefono = input("Introduce el nuevo telefono: ")
            contactos[indice]["telefono"] = new_telefono
            print("\nTelefono Actualizado.")
        elif campo == "3":
            new_email = input("Introduce el nuevo email: ")
            if "@" in new_email:
                contactos[indice]["email"] = new_email
                print("\nEmail actualizado.")
            else:
                print("\nIngrese un correo electronico valido")
        elif campo == "4":
            new_nombre = input("Introduce el nuevo nombre: ")
            new_telefono = input("Introduce el nuevo telefono: ")
            new_email = input("Introduce el nuevo email: ")
            if "@" in new_email:
                contactos[indice]["nombre"] = new_nombre
                contactos[indice]["telefono"] = new_telefono
                contactos[indice]["email"] = new_email
                print("\nCampos Actualizados.")
            else:
                print("\nIngrese un correo electronico valido")
        else:
            print("Introduzca una opcion valida.")
    else:
        print("Introduzca un numero valido")


def eliminar_contacto():
    listar_contactos()

    indice = int(input("Coloque el indice del contacto a eliminar: ")) - 1
    try:
        if 0 <= indice < len(contactos):
            contacto_eliminado = contactos.pop(indice)
            print(f"{contacto_eliminado['nombre']} eliminado")
        else:
            print("numero de contacto invalido")
    except ValueError:
        print("ingresa un numero valido")


def guardar_cargar_archivo():
    print("Que Quieres hacer: ")
    print("\n 1. Guardar contactos en Json")
    print("\n 2. Cargar contactos desde Json")
    opcion = input("\n Opcion: ")

    if opcion == "1":
        guardar_contactos()
    elif opcion == "2":
        cargar_contactos()
    else:
        print("¡Escoge una opcion valida!")


while True:
    menu()
    opcion = input("Elige una opción: ")
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        listar_contactos()
    elif opcion == "3":
        buscar_contacto(contactos)
    elif opcion == "4":
        editar_contacto()
    elif opcion == "5":
        eliminar_contacto()
    elif opcion == "6":
        guardar_cargar_archivo()
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
