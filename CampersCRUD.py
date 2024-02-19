import json

def MainCamperAñadir():
    with open('inscritos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    
    def mainCamper():
        estado = "Inscrito"
        nuevo_id = max([inscripcion["id"] for inscripcion in mijson['datos']['inscripciones']], default=0) + 1
        
        nueva_inscripcion = {}
        nueva_inscripcion['id'] = nuevo_id
        nueva_inscripcion['Identificacion'] = int(input("Escriba el número de identificación: "))
        nueva_inscripcion['Nombre'] = input("Escriba el nombre: ")
        nueva_inscripcion['Apellido1'] = input("Escriba el apellido 1: ")
        nueva_inscripcion['Apellido2'] = input("Escriba el apellido 2: ")
        nueva_inscripcion['Direccion'] = input("Escriba la dirección: ")
        nueva_inscripcion['Acudiente'] = input("Escriba el nombre de su acudiente (opcional): ")
        nueva_inscripcion['Celular'] = int(input("Escriba el número de celular: "))
        nueva_inscripcion['Telefono'] = int(input("Escriba el número de teléfono: "))
        nueva_inscripcion['Estado'] = estado

        mijson['datos']['inscripciones'].append(nueva_inscripcion)
        
        with open('inscritos.json', 'w', encoding="utf8") as file:
            json.dump(mijson, file, indent=2)
    
    mainCamper()

def MainCamperAprobados():
    with open('inscritos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    
    with open('datos.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)
    
    listainscritos = mijson['datos']['inscripciones']
    estadoA = "Aprobado"
    estadoR = "Reprobado"
    riesgoB = "Sin riesgo"
    riesgoM = "Riesgo alto"
    y = int(input("Escriba el ID del estudiante a actualizar: "))
    
    for i, inscripcion in enumerate(listainscritos):
        if inscripcion['id'] == y:
            notapractica = int(input("Digite la nota de la prueba práctica: "))
            notateorica = int(input("Digite la nota de la prueba teórica: "))
            notafinal = (notapractica + notateorica) / 2
            
            aprobado = {
                "Nombre": inscripcion['Nombre'],
                "Apellido1": inscripcion['Apellido1'],
                "Apellido2": inscripcion['Apellido2'],
                "Direccion": inscripcion['Direccion'],
                "Nombre Acudiente": inscripcion['Acudiente'],
                "Celular": inscripcion['Celular'],
                "Telefono": inscripcion['Telefono'],
                "Estado": estadoA if notafinal >= 60 else estadoR,
                "Fecha de inicio": input("Escriba la fecha de inicio del estudiante: "),
                "Fecha de finalizacion": input("Escriba la fecha de finalización: "), #Hacer que el sistema lo digite solo
                "Riesgo": riesgoB if notafinal >= 60 else riesgoM,
                "Trainer": " ",
                "Ruta" : " ",
                "Salon": " "
            }
            
            mijson2['Datos']['Matriculados'].append(aprobado)
            listainscritos.pop(i)
            
            with open('inscritos.json', 'w', encoding="utf8") as file:
                json.dump(mijson, file, indent=2)
            
            with open('datos.json', 'w', encoding="utf8") as file:
                json.dump(mijson2, file, indent=2)
            break  # Break the loop after processing one entry