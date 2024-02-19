import os
import CampersCRUD
import TrainersCRUD
import TrainersHorario
print("**************************************************")
print("*                   Bienvenido                   *")
print("**************************************************")

def limpiar_terminal():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

while True:
    limpiar_terminal()  # Limpiar la pantalla antes de mostrar el menú principal
    print("Cual es tu ROL en CAMPUSLANDS")
    print("\n1. Coordinador\t 2. Trainer\t 3. Salir")
    print(" ")
    Rol = int(input("--->"))
    if Rol == 1:
        while True:
            limpiar_terminal()
            print("**************************************************")
            print("*             Bienvenido Coordinador             *")
            print("**************************************************")
            print(" ")
            print("A cual modulo desea ingresar: ")
            print(" ")
            print("1. Camper\t2. Trainer\t")
            print("")
            print("3. Reportes\t4. Rutas\t")
            print(" ")
            print("5. Ir al modulo anterior")
            decision = int(input("--->"))
            
            if decision == 1:
                limpiar_terminal()  # Limpiar la pantalla antes de mostrar las opciones de Camper
                print("**************************************************")
                print("*                  MODULO CAMPERS                *")
                print("**************************************************")
                print(" ")
                print("1. Inscribir Camper \t 2. Matricular Camper")
                print(" ")
                print("3. Rendimiento Camper\t 4. Ir al modulo anterior")

                decision_camper = int(input("--->"))

                if decision_camper == 1:
                    limpiar_terminal()
                    print("Inscribir Camper\n")
                    print(CampersCRUD.MainCamperAñadir())
                    
                elif decision_camper == 2:
                    limpiar_terminal()
                    print("Matricular Camper")
                    print(CampersCRUD.MainCamperAprobados())
                elif decision_camper == 3:
                    limpiar_terminal()
                    print("Rendimiento Camper")
                    print ( "1. Actualizar notas finales  \t 2. Mirar lista de campers ")
                    print(" ")
                    print("3. Mirar redimiento de camper\t 4. Ir al modulo anterior")
                    decision = int(input("--->"))
                    limpiar_terminal()
                    if decision == 1:
                     print("Vamos a actualizar notas finales de los modulos")
                     x = input("")
                    elif decision == 2:
                        print("Lista notas campers")
                    elif decision == 3:
                     print("Rendimiento de camper\n")
                     print ("Que modulo desea actulizar")
                     print("")
                     print ( "1. Fundamentos de la programacion\t2. Programación Web ")
                     print(" ")
                     print("3. Programación formal\t\t\t4. Bases de datos")
                     print ("")
                     print("5. Backend")
                     decision = int(input("--->"))
                     print("")
                     if decision == 1:
                      print("Fundamentos de la programacion")
                    elif decision == 2:
                       print("Programacion web")
                    elif decision == 3:
                     print("Programacion formal")
                    elif decision == 4:
                     print("Bases de datos")
                    elif decision == 5:
                     print("Backend")
                    else:
                     print("Opción inválida")


                elif decision_camper == 4:
                    print("Salir")
                else:
                    print("Opción inválida")

            elif decision == 2:
                limpiar_terminal()
                print("**************************************************")
                print("*                MODULO TRAINERS                 *")
                print("**************************************************")
                print(" ")
                print("1. Añadir Trainer \t 2. Eliminar Trainer")
                print(" ")
                print("3. Asignar Trainer\t 4. Salir")

                decision = int(input("--->"))

                if decision == 1:
                    print("Añadir Trainer")
                    print(TrainersCRUD.MainTrainersAñadir())
                elif decision == 2:
                    print("Eliminar Trainer")
                    print(TrainersCRUD.MainTrainersEliminar())
                elif decision == 3:
                    print("Asignar Trainer")
                elif decision == 4:
                    print("Ir al modulo anterior")
                else:
                    print("Opción inválida")
            elif decision == 3:
                limpiar_terminal()
                print("**************************************************")
                print("*                MODULO REPORTES                 *")
                print("**************************************************")
                print(" ")
                print("1. Campers que se encuentren en estado de INSCRITO")
                print("2. Campers que aprobaron el examen inicial ")
                print("3. Trainers Activos")
                print("4. Campers que se encuentren con bajo rendimiento")
                print("5. Campers y Trainers asociados a una ruta de entrenamiento")
                print("6. Campers aprobados y desaprobados")
                print("7. Ir al modulo anterior")

                decision = int(input("--->"))

                if decision == 1:
                    print("Campers en estado de INSCRITO")
                elif decision == 2:
                    print("Campers que aprobaron el examen inicial")
                elif decision == 3:
                    print("Trainers Activos")
                elif decision == 4:
                    print("Campers con bajo rendimiento")
                elif decision == 5:
                    print("Campers y Trainers asociados a una ruta de entrenamiento")
                elif decision == 6:
                    print("Campers aprobados y desaprobados")
                elif decision == 7:
                    print("")
                else:
                    print("Opción inválida")
            elif decision == 4:
                print("**************************************************")
                print("*                MODULO RUTAS                    *")
                print("**************************************************")
                print("")
                print("1. Añadir Rutas  \t 2. Ir al modulo anterior")
                print(" ")
                decision_ruta=int(input("------>"))
            elif decision==5:
                break
            else:
                print("Decision no valida")
    elif Rol == 2:
        while True:
            limpiar_terminal()
            print("**************************************************")
            print("*             Bienvenido Trainer                 *")
            print("**************************************************")
            print(" ")
            print("A cual modulo desea ingresar: ")
            print(" ")
            print("1. Mostrar Horario\t2. Ir al modulo anterior\t")
            print("")
            decision = int(input("--->"))
            
            if decision == 1:
                limpiar_terminal()
                print(TrainersHorario.HorarioTrainers())
            elif decision == 2:
                break
            else:
                print("Decision no valida")
    elif Rol == 3:
        break