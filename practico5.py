def agregar_alumnos(alumno_nuevo):
    name=alumno_nuevo
    surname= input("Ingrese el apellido del alumno:")
    doc= int(input("Ingrese el DNI del alumno:"))
    dat= input("Ingrese la fecha de nacimiento del alumno:")
    tut= input("Ingrese el nombre del tutor del alumno:")
    inas= input("Ingrese las inasistencias del alumno:")
    amon= int(input("Ingrese la cantidad de amonestaciones del alumno:"))


    alumno_nuevo={"NOMBRE": name,
         "APELLIDO" : surname,
         "DNI" : doc,
         "DATE": dat,
         "TUTOR" : tut,
         "FALTAS" : inas,
         "AMONESTACIONES" : amon}
    

    registro_escolar["Alumnos"].append(alumno_nuevo)
    
def modificar_alumno(alumno_para_modificar):
    name=input("Ingrese el nuevo nombre del alumno:")
    surname= input("Ingrese el nuevo apellido del alumno:")
    doc= int(input("Ingrese el nuevo DNI del alumno:"))
    dat= input("Ingrese la nueva fecha de nacimiento del alumno:")
    tut= input("Ingrese el nuevo nombre del tutor del alumno:")
    inas= input("Ingrese las inasistencias del alumno:")
    amon= int(input("Ingrese la cantidad de amonestaciones del alumno:"))


    alumno_para_modificar={"NOMBRE": name,
         "APELLIDO" : surname,
         "DNI" : doc,
         "DATE": dat,
         "TUTOR" : tut,
         "FALTAS" : inas,
         "AMONESTACIONES" : amon}

cantidad_de_alumnos = 3

gabriel={"NOMBRE": "Gabriel",
         "APELLIDO" : "Touceda",
         "DNI" : "48984123",
         "DATE": "24/07/2005",
         "TUTOR" : "Jorgelina Matambre",
         "FALTAS" : "2",
         "AMONESTACIONES" : "0"}

nazarena={"NOMBRE": "Nazarena",
         "APELLIDO" : "Fernandez",
         "DNI" : "47957324",
         "DATE": "02/11/2003",
         "TUTOR" : "Camila Ituzaingo",
         "FALTAS" : "1",
         "AMONESTACIONES" : "1"}

pedro={"NOMBRE": "Pedro",
         "APELLIDO" : "Salvadores",
         "DNI" : "49444876",
         "DATE": "10/02/2008",
         "TUTOR" : "Jose de la Cruz",
         "FALTAS" : "13",
         "AMONESTACIONES" : "2"}

registro_escolar = {"Alumnos": [gabriel, nazarena, pedro]}

print("Buenas, bienvenido al registro escolar")
print("Si desea ver los datos que posee el registro ingrese 1.")
print("Si desea ver los datos de un alumno en concreto ingrese 2")
print("Si desea modificar los datos de un alumno ingrese 3")
print("Si desea agregar un alumno ingrese 4")
print("Si desea remover un alumno ingrese 5")
print("Si desea salir del programa ingrese 6")

while True:
    desicion=int(input("Que desea hacer?:"))
    if desicion == 1:
        for alumno in registro_escolar["Alumnos"]:
           print(f"{alumno['NOMBRE']} {alumno['APELLIDO']}")
    elif desicion == 2:
        alumno_visto = input("Ingrese SOLO el nombre del alumno:").lower()
        alumno_encontrado = next((alumno for alumno in registro_escolar["Alumnos"] if alumno["NOMBRE"].lower() == alumno_visto), None)
        if alumno_encontrado:
             print(f"INFORMACION DE {alumno_visto.upper()}: {alumno_encontrado}")
        else:
            print("El nombre del alumno ingresado no se encuentra en la base de datos del registro escolar")
    elif desicion == 3:
        alumno_a_modificar = input("Ingrese el nombre del alumno al que desee modificar:").lower()
        alumno_por_moficar = next((alumno for alumno in registro_escolar["Alumnos"] if alumno["NOMBRE"].lower() == alumno_a_modificar), None)
        if alumno_por_moficar:
            modificar_alumno(alumno_a_modificar)
        else:
            print("No se encuentra el nombre del alumno en el registro")
    elif desicion == 4:
        alumno_agregado = str(input("Ingrese SOLO el nombre del alumno para agregar al registro:")).lower()
        if " " in alumno_agregado:
            print("Error, ingresa SOLO el nombre principal")
        elif next((alumno for alumno in registro_escolar["Alumnos"] if alumno["NOMBRE"].lower() == alumno_agregado), None):
            print("Ya hay un alumno con ese mismo nombre en el registro, porfavor agrega algo para diferenciarlos(Puede ser la inicial de su apellido al final del nombre)")
        else:
            agregar_alumnos(alumno_agregado)
    elif desicion == 5:
        alumno_a_remover= input("Ingrese SOLO el nombre del alumno por remover:").lower()
        if " " in alumno_a_remover:
            print("Error, ingresa SOLO el nombre del alumno de acuerdo a como se encuentre en el registro")
        else:
            alumno_removido = next((alumno for alumno in registro_escolar["Alumnos"] if alumno["NOMBRE"].lower() == alumno_a_remover), None)
            if alumno_removido:
               registro_escolar["Alumnos"].remove(alumno_removido)
               print(f"El alumno {alumno_a_remover} ha sido removido del registro")
            else:
               print("No se encontro el nombre del alumno, porfavor revise de nuevo.")
    elif desicion == 6:
            print("Gracias por utilizar nuestro registro escolar.")
            break





