import json

def matriculados():
    with open('datos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)

    with open('Matriculados.json', 'r', encoding="utf8") as file:
        mijson2 = json.load(file)

    matriculados_aprobados = []

    for i in mijson["Datos"]["Matriculados"]:
        if i["Estado"] == "Aprobado":
            aprobado = {
                "Nombre": i['Nombre'],
                "Apellido1": i['Apellido1'],
                "Apellido2": i['Apellido2'],
                "Direccion": i['Direccion'],
                "Nombre Acudiente": i['Acudiente'],
                "Celular": i['Celular'],
                "Telefono": i['Telefono'],
                "Estado": i['Estado'],
                "Fecha de inicio": i['Fecha de inicio'],
                "Fecha de finalizacion": i['Fecha de finalizacion'],
                "Riesgo": i['Riesgo'],
                "Trainer": " ",
                "Ruta": " ",
                "Salon": " "
            }
            mijson2['Datos']['Matriculados'].append(aprobado)

    with open('MatriculadosAprobados.json', 'w', encoding="utf8") as file:
        json.dump(matriculados_aprobados, file, ensure_ascii=False, indent=4)





        
    
