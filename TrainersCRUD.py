import json
def MainTrainersAñadir():
  
    try:
        with open('datos.json', 'r', encoding="utf8") as file:
            mijson = json.load(file)
    except FileNotFoundError:
        mijson = {"Datos": {"Trainers_Secundarios": []}}
    
    if 'Trainers_Secundarios' not in mijson['Datos']:
        mijson['Datos']['Trainers_Secundarios'] = []
        
    nuevo_id = max([inscripcion["id"] for inscripcion in mijson['Datos']['Trainers_Secundarios']], default=0) + 1
    nueva_inscripcion = {}
    nueva_inscripcion['id'] = nuevo_id + 3 if nuevo_id == 1 else nuevo_id
    nueva_inscripcion['Identificacion'] = int(input("Escriba el número de identificación: "))
    nueva_inscripcion['Nombre'] = str(input("Escriba el nombre: "))
    nueva_inscripcion['Apellido1'] = input("Escriba el apellido 1: ")
    nueva_inscripcion['Celular'] = int(input("Escriba el número de celular: "))
    nueva_inscripcion['Telefono'] = int(input("Escriba el número de teléfono: "))
    nueva_inscripcion['Horario'] = {
          "Clase1" : "Sin asignar",
          "Clase2" : "Sin asignar",
          "Clase3" : "Sin asignar",
          "Clase4" : "Sin asignar"
          }
    
    mijson['Datos']['Trainers_Secundarios'].append(nueva_inscripcion)
    
    with open('datos.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=2)


def MainTrainersEliminar():
    identificacion_a_eliminar = int(input("Ingrese el número de identificación del entrenador a eliminar: "))
    import json
    with open('datos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
        
    if identificacion_a_eliminar <= 3:
        entrenadores = mijson['Datos']['Trainer_Principales']
        for entrenador in entrenadores:
            if entrenador['id'] == identificacion_a_eliminar:
                entrenador['Identificacion'] = ''
                entrenador['Nombre'] = ''
                entrenador['Apellido1'] = ''
                entrenador['Celular'] = ''
                entrenador['Telefono'] = ''
    else:
        entrenadores = mijson['Datos']['Trainers_Secundarios']
        
        indice_a_eliminar = None
        for i, entrenador in enumerate(entrenadores):
            if entrenador['Identificacion'] == identificacion_a_eliminar:
                indice_a_eliminar = i
                break
            
        if indice_a_eliminar is not None:
            del mijson['Datos']['Trainers_Secundarios'][indice_a_eliminar]
            print("Entrenador eliminado exitosamente.")
        else:
            print("No se encontró ningún entrenador con la identificación proporcionada.")
        
    with open('datos.json', 'w', encoding="utf8") as file:
        json.dump(mijson, file, indent=2)


def MainAsignarTrainers():
    import json
    
    with open('datos.json', 'r', encoding="utf8") as outfile:
        mijson = json.load(outfile)
    
    TrainersP = mijson['Datos']['Trainer_Principales']
    print("Estos son los puestos de Trainers principales que están desocupados en este momento:\n")
    
    for i, trainer in enumerate(TrainersP, start=1):
        if not trainer['Nombre']:
            print(f"Puesto #{i} desocupado")
        else:
            print(f"Puesto #{i} ocupado")
    
    añadir = int(input("En cuál de los espacios deseas añadir al trainer (1, 2 o 3): "))
    
    if añadir in [1, 2, 3]:
        if not TrainersP[añadir - 1]['Nombre']:
            print("Añadiendo trainer...")
            # Aquí puedes añadir el código para añadir un nuevo trainer
        else:
            print("Puesto ocupado")
            
    else:
        print("Opción inválida. Debes seleccionar 1, 2 o 3.")

