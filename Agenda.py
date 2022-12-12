from os import system

class agenda:
    def __init__ (self):
        self.lista = []

    def agregar(self):
        #Guardar Tarea en variable
        nuevaTarea = str(input("Añadir tarea: "))
        #Añadir a Array de tareas
        self.lista.append(nuevaTarea)
        #Abrir Documento
        doc = open("Agenda.txt", "w")
        #Llenar Documento
        doc.write(str(self.lista) + "\n")
        #Cerrar Documento
        doc.close()

    def eliminar(self):
        print("Tareas Actuales:")
        #Abrir Documento
        doc = open("Agenda.txt", "r")
        #Mostrar Tareas Guardadas en el documento
        print(doc.read())
        #Cerrar Documento
        doc.close()
        #Guar Tarea a eliminar en variable
        eliminarTarea = str(input("\nEliminar tarea: "))
        #Evaluar existencia de tarea en array de tareas
        if eliminarTarea in self.lista:
            #Limpiar pantalla
            system("cls")
            #Si existe se obtiene el indice
            tareaEliminada = self.lista.index(eliminarTarea)
            #Eliminar Tarea
            self.lista.pop(tareaEliminada)
            #Abrir Documento
            doc = open("Agenda.txt","w")
            #Sobreescribir documento
            doc.write(str(self.lista))
            #Cerrar Documento
            doc.close()
            #Mensaje de tarea Eliminada
            print("Se elimino la tarea: ",eliminarTarea)
        else:
            #Limpiar pantalla
            system("cls")
            #Si no existe la tarea en el array se informa al usuario
            print("No hay una tarrea llamada: ",eliminarTarea)

    def mostrar(self):
        print("Lista de Tareas:")
        #Abrir Documento
        doc = open("Agenda.txt", "r")
        #Mostrar tareas en el Documento
        print(doc.read())
        #Cerrar Documento
        doc.close()

    def limpiar(self):
        #Abrir Documento
        doc = open("Agenda.txt","w")
        #Sobre escribir documento para vaciarlo
        doc.write("")
        #Cerrar Documento vaciado
        doc.close()


#Menu de Opciones
#Limpiado de consola inicial
system("cls")
#Peticion de accion
opcion=input("¿Que desea Hacer?\nAgregar tarea: 1\nEliminar tarea: 2\nVer lista de tareas: 3\nSalir: cualquier otra tecla\n")
#Guardar clase en variable para llamar metodos en bucle
AGENDA=agenda()
#Inicio de Bucle
while opcion == "1" or opcion == "2" or opcion == "3":
    #Match / Case para evaluar accion a ejecutar
    match opcion:
        #Si la opcion es 1
        case "1":
            #Limpiar texto en pantalla
            system("cls")
            #Llamar Medoto de Agregar tarea
            AGENDA.agregar()
        #Si la opcion es 2
        case "2":
            #Limpiar pantalla
            system("cls")
            #Llamar metodo de elimiar tarea
            AGENDA.eliminar()
        #Si la opcion es 3
        case "3":
            #Limpiar pantalla
            system("cls")
            #Llamar metodo de Mostrar lista de tareas
            AGENDA.mostrar()
    #Seleccion de opcion que determina permanencia de buble
    opcion=input("\n\n¿Que desea Hacer?\nAgregar tarea: 1\nEliminar tarea: 2\nVer lista de tareas: 3\nSalir: cualquier otra tecla\n")

#Validacion de Accion ingresada para Cerrar proceso y limpiar Documento
if opcion != "1" or opcion != "2" or opcion != "3" :
    #Llamada de metodo para limpiar
    AGENDA.limpiar()
    #Mensaje de cierre
    print("Gracias por usar esta App!")