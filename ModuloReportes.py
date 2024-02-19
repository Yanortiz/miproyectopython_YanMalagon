def Listainscritos ():
    import json
    x=open("inscritos.json" , 'r')
    mijson= json.load (x)
    print (" Por favor de enter para mostrar Campers en estado inscrito")
    listains=mijson[ "datos"]["inscripciones"]
    for i in listains:
        for llave,valor in i.items():
             print (f"{llave}: {valor}")
        print("-------------------------\n")





def ListaAprobaronExamen():
    import json
    
    with open("datos.json", 'r') as x:
        data = json.load(x)
    
    listaaprobaron = [camper for camper in data["Datos"]["Matriculados"] if camper["Estado"] == "Aprobado"]

    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el examen inicial")

    for camper in listaaprobaron:
        for llave, valor in camper.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")


def listatrainerscampus():
    import json
    x=open("datos.json", 'r')
    data = json.load(x)

    listatrainers= data["Datos"]["Trainer_Principales"]
    print("Por favor, presiona Enter si deseas visualizar los campers que aprobaron el examen inicial")
    enter = input("")

    for trainers in listatrainers:
        for llave, valor in trainers.items():
            print (f"{llave}: {valor}")
        print("-------------------------\n")