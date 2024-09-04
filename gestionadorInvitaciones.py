
def gestionadorInvitaciones():
    
    invitados = []
    
    def agregarInvitado():
        nombreInvitado = input("Digite el nombre de invitado: ").capitalize()
        invitados.append(nombreInvitado)
        print("Se realizo la invitacion con exito\n")
    
    def eliminarInvitado():
        nombreInvitado = input("Digite el nombre de invitado que desea eliminar: ").capitalize()
        if nombreInvitado in invitados:
            invitados.remove(nombreInvitado)
            print("Se elimino la invitación con exito\n")
        else:
            print("El nombre indicado no existe en la lista\n")
    
    def verificarInvitado():
        nombreInvitado = input("Digite el nombre de invitado a verificar: ").capitalize()
        if nombreInvitado in invitados:
            print(f"{nombreInvitado} ya esta en la lista de invitados\n")
        else:
            print(f"{nombreInvitado} no esta en la lista")
            opc = input("¿Desea invitarlo?\nDigite Si o No\n")
            if opc.lower() == "si":
                agregarInvitado()
            else:
                print(f"{nombreInvitado} no sera invitado a la fiesta")
    
    def editarInvitado():
        nombreInvitado = input("Digite el nombre de invitado a editar: ").capitalize()
        if nombreInvitado in invitados:
            index = invitados.index(nombreInvitado)
            nombreInvitado = input("Digite el nuevo nombre: ")
            invitados[index] = nombreInvitado
            print(f"{nombreInvitado} se actualizo con exito\n")
        else:
            print(f"{nombreInvitado} no esta en la lista")
            opc = input("¿Desea invitarlo?\nDigite Si o No\n")
            if opc.lower() == "si":
                agregarInvitado()
            else:
                print(f"{nombreInvitado} no sera invitado a la fiesta\n")
                
    def mostrarInvitados():
        for i, invitado in enumerate(invitados, start=1):
            print(f"{i}: {invitado}")
        print("\n")
    
    def menuGestionInvitados():
        while True:
            print("** ORGANIZANDOR DE FIESTA **")
            print(f"1 => Agregar un invitado\n"
                "2 => Eliminar un invitado\n"
                "3 => Verificar un invitado\n"
                "4 => Editar un invitado\n"
                "5 => Mostar todos los invitados\n"
                "6 => Salir")
            
            opc = int(input("Ingrese la opcion deseada: "))

            if opc == 1:
                agregarInvitado()
            elif opc == 2:
                eliminarInvitado()
            elif opc == 3:
                verificarInvitado()
            elif opc == 4:
                editarInvitado()
            elif opc == 5:
                mostrarInvitados()
            elif opc == 6:
                break
            else:
                print("Digite una opción correcta\n")
    
    return menuGestionInvitados()

gestionadorInvitaciones()