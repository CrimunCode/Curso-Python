def mostrar_menu():
    print("\nAgenda de contactos:\n")
    print("(Seleccione una opción del menu)\n")
    print("C. Crear nuevo contacto")
    print("V. Ver todos los contactos")
    print("B. Buscar un contacto")
    print("E. Eliminar un contacto")
    print("S. Salir de la agenda")
    print("\n")


def crear_contacto(agenda):
    nombre = input("Ingrese el nombre completo del contacto: ".upper())
    telefono = input("Ingrese el teléfono del contacto: ")
    email = input("Ingrese el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha creado el contacto {nombre} exitosamente!")


def ver_concatos(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre, info in agenda.items():
            print(f"Nombre   : {nombre}")
            print(f"Teléfono : {info["telefono"]}")
            print(f"Email    : {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda está vacía")


def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ".upper())
    if nombre in agenda:
        print(f"Nombre   : {nombre}")
        print(f"Teléfono : {agenda[nombre]["telefono"]}")
        print(f"Email    : {agenda[nombre]["email"]}")
    else:
        print(f"El contacto {nombre} no está registrado")


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ".upper())
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado de la agenda")
    else:
        print(f"No se ha encontrado el contacto con el nombre: {nombre.upper()}")


def agenda_contactos():
    agenda = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elija un opción: ")
        
        if opcion == "c":
            crear_contacto(agenda)
        elif opcion == "v":
            ver_concatos(agenda)
        elif opcion == "b":
            buscar_contacto(agenda)
        elif opcion == "e":
            eliminar_contacto(agenda)
        elif opcion == "s":
            print("Saliendo de la agenda ¡Hasta luego!")
            break
        else:
            print("Por favor ingrese una opción válida")

agenda_contactos()