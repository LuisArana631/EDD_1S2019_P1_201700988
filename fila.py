import os

class Nodo:
    def __init__(self, nombre=None, punteo=None):
        self.nombre = nombre
        self.punteo = punteo
        self.atras = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.longitud = 0

    def fila_vacia(self):
        return self.inicio == None

    def insertar(self, nombre, punteo):
        nuevo = Nodo(nombre, punteo)
        if self.fila_vacia() == True:
            self.inicio = nuevo
        else:
            self.fin.atras = nuevo
        self.fin = nuevo

    def registros(self):
        return self.longitud

    def eliminar(self):
        if self.fila_vacia() != True:
            temp = self.inicio.atras
            self.inicio.atras = None
            self.inicio = temp

    def mostrar_fila(self):
        if self.fila_vacia() == True:
            print("Esta vacia la fila")
        else:
            temp = self.inicio
            while temp is not None:
                print(temp.nombre,",",str(temp.punteo),"|")
                temp = temp.atras


    def graficar(self):
        if self.fila_vacia() == True:
            print("Esta vacia la fila")
        else:
            archivo = open("scoreReporte.dot", "w")
            archivo.write("digraph score {\n")
            archivo.write("label=\"Score de usuarios\";\n")
            archivo.write("rankdir=LR\n")
            archivo.write("graph [fontsize=18 fontname=\"Verdana\" compound=true];\n")
            archivo.write("node [shape=record fontsize=18 fontname=\"Verdana\"]\n")

            temp = self.inicio     
            conteo = 0       
            while temp is not None:
                archivo.write("\"node")
                archivo.write(str(conteo))
                archivo.write("\"[label = \"{<f0> (")
                archivo.write(temp.nombre)
                archivo.write(",")
                archivo.write(str(temp.punteo))
                archivo.write(")|<f1>}\"];\n")
                if temp.atras is not None:
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f1 -> \"node")
                    conteo = conteo +1
                    archivo.write(str(conteo))
                    archivo.write("\":f0;\n")
                else:
                    archivo.write("nodenull[label = \"<f0> null\"];\n")
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f1 -> \"nodenull\":f0;\n")
                temp = temp.atras
            
            archivo.write("}")
            archivo.close()

            os.system("dot -Tpng scoreReporte.dot -o scoreReporte.png")
            os.system("scoreReporte.png")
