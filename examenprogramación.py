# EXAMEN PROGRAMACIÓN PRIMERA EVALUACIÓN
# Desenvolupa una aplicació amb Python que permeti gestionar una classificació d’equips i les seves puntuacions.

#Aquí he usado append para añadir un nuevo equipo a la clasificación.
def newTeam(equip, classificacio):
    classificacio.append([equip, 0])

#Aquí he definido que cuando el usuario introduzca una posición y una puntuación se actualice la puntuación del equipo.
def updateTeam(posicio, puntuacio, classificacio):
    if 1 <= posicio <= len(classificacio):
        classificacio[posicio - 1][1] = puntuacio
    else:
        print("Posició no valida")

#Aquí he utilizado la función pop para eliminar un equipo de la clasificación.
def deleteTeam(posicio, classificacio):
    if 1 <= posicio <= len(classificacio):
        classificacio.pop(posicio - 1)
    else:
        print("Posició no valida")

#Aqui he utilizado el método de la burbuja para ordenar la clasificación. 
def updateLeague(classificacio):
    for i in range(len(classificacio)):
        for j in range(len(classificacio)):
            if classificacio[i][1] > classificacio[j][1]:
                classificacio[i], classificacio[j] = classificacio[j], classificacio[i]

#Aqui se imprimirá la clasificación en orden.
def viewLeague(classificacio):
    for i in range(len(classificacio)):
        print(str(i + 1) + ".   " + classificacio[i][0] + "      " + str(classificacio[i][1]) + "  punts")

#Aqui he definido menú para mostrar las opciones del menú.
def menu():
    print("****************")
    print("     MENÚ")
    print("****************")
    print("1. Introdueix un equip")
    print("2. Actualizar puntuació d'equip")
    print("3. Eliminar equip")
    print("4. Veure classificació")
    print("5. Sortir")
    print("****************")


classificacio = []
menu()
opcio = int(input("Introdueix una opció: "))

#Aqui he utilizado un bucle while para que el menú se repita hasta que el usuario decida salir cuando introduzca el número 5.
while opcio != 5:
    #Aquí se introduce un nuevo equipo en la clasificación cuando el usuario introduce el número 1.
    if opcio == 1:
        equip = input("Introdueix el nom del nou equip: ")
        newTeam(equip, classificacio)
        print("Mallorca ha estat introduit a la classificació")
    #Aquí se cambia la puntuación de un equipo cuando el usuario introduce el número 2. 
    elif opcio == 2:
        updateLeague(classificacio)
        viewLeague(classificacio)
        posicio = int(input("Introdueix la posició de l'equip: "))
        puntuacio = int(input("Introdueix la puntuació de l'equip: "))
        updateTeam(posicio, puntuacio, classificacio)
    #Aquí se elimina un equipo de la clasificación cuando el usuario introduce el número 3.
    elif opcio == 3:
        viewLeague(classificacio)
        posicio = int(input("Introdueix la posició de l'equip a borrar: "))
        deleteTeam(posicio, classificacio)
    #Aquí se ordena que cuando el usuario introduzca el número 4 se imprima la clasificación por pantalla. 
    elif opcio == 4:
        updateLeague(classificacio)
        viewLeague(classificacio)
    menu()
    opcio = int(input("Introdueix una opció: ")) 

print("Adiós :)")