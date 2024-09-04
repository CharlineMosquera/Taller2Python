from datetime import datetime

def verificadorEdades():
    edad = int(input("¿Cual es su edad? "))
    fechaAcual = datetime.now()
    anioActual = fechaAcual.year
    anioNacimiento = anioActual - edad
    
    def mayorEdad(age):
        if age >= 18:
            print(f"¡Eres mayor de edad, Felicitaciones!")
        else:
            aniosParaMayor = 18 - age
            print(f"¡No eres mayor de edad y te faltan {aniosParaMayor} años para serlo!")
            
    def generaciones(anio):
        mensaje = ""
        if 1928 <= anio <= 1944:
            mensaje = "Perteneces a la Generación Silent"
        elif 1945 <= anio <= 1964:
            mensaje = "Perteneces a la Generación Baby Boomers"
        elif 1965 <= anio <= 1981:
            mensaje = "Perteneces a la Generación X"
        elif 1982 <= anio <= 1994:
            mensaje = "Perteneces a la Generación Y o Millennials"
        elif 1995 <= anio <= 2009:
            mensaje = "Perteneces a la Generación Z o Centennials"
        elif 2010 <= anio <= 2024:
            mensaje = "Perteneces a la Generación Alfa"
        else:
            mensaje = "Tu generación no esta determinada"
        print(mensaje)
        
    def condicionesEspeciales(age):
        if age % 10 == 0:
            print("¡¡EUREKA!! Tu edad es un número redondo ^_^")
            
    def mensajeFinal():
        print(f"Descubrimos que con tu edad de {edad} años")
        mayorEdad(edad)
        generaciones(anioNacimiento)
        condicionesEspeciales(edad)
    
    return mensajeFinal()
    
verificadorEdades()
