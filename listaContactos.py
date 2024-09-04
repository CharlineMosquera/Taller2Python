def listaContactos():
    
    contactos = {}
    
    def agregarContacto():
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el número de teléfono: "))
        contactos[nombre] = telefono
        print("Se añadio con exito el contacto\n")
        
    def buscarContacto():
        nombreBuscado = input("Ingrese el nombre del contacto buscado: ")
        if nombreBuscado in contactos:
            telefonoBuscado = contactos[nombreBuscado]
            print(f"El teléfono de {nombreBuscado} es {telefonoBuscado}\n")
        else:
            print("El nombre que ingreso no existe en la lista\n")
        
    def mostrarContactos():
        for i, (nombre, telefono) in enumerate(contactos.items(), start=1):
            print(f"Contacto {i} Nombre: {nombre} - Teléfono: {telefono}")
        print("\n")
        
    def editarContacto():
        contactoEditar =  input("Ingrese el nombre del contacto a actualizar: ")
        if contactoEditar in contactos:
            telefonoEditar = int(input("Ingrese el nuevo número de teléfono: "))
            contactos[contactoEditar] = telefonoEditar
            print(f"El teléfono de {contactoEditar} se actualizo con exito\n")
        else:
            print("El nombre que ingreso no existe en la lista\n")
    
    def menuListaContactos():
        while True:
            print("** LISTA DE CONTACTOS **")
            print(f"1 => Agregar nuevo contacto\n"
                "2 => Buscar contacto\n"
                "3 => Mostrar todos los contactos\n"
                "4 => Editar teléfono de un contacto\n"
                "5 => Salir")
            
            opc = int(input("Ingrese la opcion deseada: "))

            if opc == 1:
                agregarContacto()
            elif opc == 2:
                buscarContacto()
            elif opc == 3:
                mostrarContactos()
            elif opc == 4:
                editarContacto()
            elif opc == 5:
                break
            else:
                print("Digite una opción correcta\n")
        
    return menuListaContactos()

listaContactos()