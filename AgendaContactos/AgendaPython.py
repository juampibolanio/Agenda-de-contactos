#TRABAJO INTEGRADOR FINAL CURSO PYTHON UTN FRRE
#BOLANIO JUAN PABLO - DNI: 46964660

import os #BIBLIOTECA PARA INTERACTUAR CON EL SISTEMA OPERATIVO, MANEJAR ARCHIVOS, DIRECTORIOS, ETC.

# INICIALIZAMOS LA LISTA DE CONTACTOS
listaContactos = []

# FUNCIONES PRINCIPALES DEL PROGRAMA

def mostrar_menu():  # MOSTRAMOS EL MENÚ AL USUARIO
    print("\n===== Menú de Agenda =====")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar un contacto")
    print("4. Modificar un contacto")
    print("5. Eliminar un contacto")
    print("6. Guardar contactos en archivo")
    print("7. Cargar contactos desde archivo")
    print("8. Salir")
    return input("- Seleccione una opción: ")

def agregar_contacto():  # FUNCION PARA AGREGAR UN CONTACTO
    print("\n===== Agenda de contactos =====")
    nombreContacto = input("- Ingrese el nombre del contacto: ")

    # COMPROBAMOS LOS DUPLICADOS
    for contacto in listaContactos:
        if contacto["Nombre"].lower() == nombreContacto.lower():
            print("Ya existe un contacto con ese nombre. Intente con otro nombre.")
            return

    numTelefono = input("- Ingrese el número de teléfono: ")
    if not numTelefono.isdigit() or len(numTelefono) != 10:
        print("El número de teléfono debe tener 10 dígitos numéricos.")
        return

    direccion = input("- Ingrese el domicilio: ")

    try: #VERIFICACION DE DATOS
        edad = int(input("- Ingrese la edad: "))
        if edad <= 0:
            print("La edad debe ser un valor positivo.")
            return
    except ValueError:
        print("La edad debe ser un número.")
        return

    # GUARDADO DEL CONTACTO
    datosContacto = {
        "Nombre": nombreContacto, 
        "NumTelefono": numTelefono, 
        "Direccion": direccion, 
        "Edad": edad
    }
    
    # SE AGREGA EL CONTACTO SI SE VALIDARON LOS DATOS
    listaContactos.append(datosContacto)
    print(f"Contacto '{nombreContacto}' agregado exitosamente.")
    ordenar_contactos()

def ver_contactos():  # FUNCIÓN PARA VER TODOS LOS CONTACTOS
    if not listaContactos:
        print("No hay contactos guardados.")
        return

    print("\n===== Lista de contactos =====")
    for i, contacto in enumerate(listaContactos, start=1):
        print(f"\nContacto {i}:")
        for clave, valor in contacto.items():
            print(f"  {clave}: {valor}")

def buscar_contacto():  # FUNCION PARA BUSCAR UN CONTACTO
    nombre_a_buscar = input("- Ingrese el nombre del contacto a buscar: ")
    encontrado = False
    for contacto in listaContactos:
        if contacto["Nombre"].lower() == nombre_a_buscar.lower():
            print("\n===== Contacto encontrado =====")
            for clave, valor in contacto.items():
                print(f"  {clave}: {valor}")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontró un contacto con el nombre '{nombre_a_buscar}'.")

def modificar_contacto():  # FUNCION PARA MODIFICAR UN CONTACTO DE LA LISTA
    nombre = input("- Ingrese el nombre del contacto que desea modificar: ")
    for contacto in listaContactos:
        if contacto["Nombre"].lower() == nombre.lower():
            nuevo_numero = input("- Ingrese el nuevo número de teléfono (10 dígitos): ")
            if not nuevo_numero.isdigit() or len(nuevo_numero) != 10:
                print("Número de teléfono inválido.")
                return
            contacto["NumTelefono"] = nuevo_numero
            print(f"Contacto '{nombre}' actualizado con éxito.")
            return
    print(f"No se encontró un contacto con el nombre '{nombre}'.")

def eliminar_contacto():  # FUNCION PARA ELIMINAR UN CONTACTO DE LA LISTA
    nombre = input("- Ingrese el nombre del contacto que desea eliminar: ")
    for contacto in listaContactos:
        if contacto["Nombre"].lower() == nombre.lower():
            listaContactos.remove(contacto)
            print(f"Contacto '{nombre}' eliminado.")
            return
    print(f"No se encontró un contacto con el nombre '{nombre}'.")

def ordenar_contactos():  # FUNCION PARA ORDENAR LOS CONTACTOS ALFABETICAMENTE
    listaContactos.sort(key=lambda x: x["Nombre"])

def guardar_contactos_en_archivo():  # FUNCION PARA GUARDAR CONTACTOS EN ARCHIVO DE TEXTO
    with open("contactos.txt", "w") as archivo:
        for contacto in listaContactos:
            archivo.write(f"{contacto['Nombre']},{contacto['NumTelefono']},{contacto['Direccion']},{contacto['Edad']}\n")
    print("Contactos guardados en 'contactos.txt'.")

def cargar_contactos_desde_archivo():  # FUNCION PARA CARGAR CONTACTOS DESDE UN ARCHIVO TXT (Contactos.txt)
    if not os.path.exists("contactos.txt"):
        print("No existe un archivo de contactos.")
        return

    with open("contactos.txt", "r") as archivo:
        for linea in archivo:
            nombre, numTelefono, direccion, edad = linea.strip().split(",")
            datosContacto = {
                "Nombre": nombre,
                "NumTelefono": numTelefono,
                "Direccion": direccion,
                "Edad": int(edad)
            }
            listaContactos.append(datosContacto)
    ordenar_contactos()
    print("Contactos cargados exitosamente.")

# PROGRAMA PRINCIPAL
while True:
    opcion = mostrar_menu()

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        modificar_contacto()
    elif opcion == "5":
        eliminar_contacto()
    elif opcion == "6":
        guardar_contactos_en_archivo()
    elif opcion == "7":
        cargar_contactos_desde_archivo()
    elif opcion == "8":
        print("Saliendo de la agenda.")
        break
    else:
        print("Opción inválida, intente de nuevo.")
        
#para cargar archivos en el programa, el mismo debe llamarse contactos.txt
