import os

class Nodo:
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class ListaDobleCircular:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.longitud = 0

    def lista_vacia(self):
        return self.inicio == None

    def insertar(self, nombre):
        nuevo = Nodo(nombre)
        if self.lista_vacia()==True:
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.inicio = nuevo
            self.fin = nuevo            
        else:
            nuevo.anterior = self.fin
            nuevo.siguiente = self.inicio
            self.fin.siguiente = nuevo
            self.inicio.anterior = nuevo
            self.fin = nuevo
        print(self.longitud)
        self.longitud = self.longitud + 1    
        print(self.longitud)

    def mostrar_nombre(self, pos):
        aux = self.inicio
        conteo = 0
        if pos < self.longitud:
            while conteo < pos:
                aux = aux.siguiente
                conteo = conteo + 1
            return aux.nombre

    def mostrar_lista(self):
        if self.lista_vacia() == True:
            print("Lista doble circular vacia")
        else:
            temp = self.inicio 
            print(temp.nombre,"|")
            temp  = temp.siguiente
            while temp != self.inicio:
                print(temp.nombre,"|")
                temp  = temp.siguiente

    def graficar(self):
        if self.lista_vacia() == True:
            print("Lista doble circular vacia")
        else:
            archivo = open("usuariosReporte.dot", "w")
            archivo.write("digraph usuarios  {\n")
            archivo.write("label=\"Listado de usuarios\";\n")
            archivo.write("rankdir=LR\n")
            archivo.write("graph [fontsize=18 fontname=\"Verdana\" compound=true];\n")
            archivo.write("node [shape=record fontsize=18 fontname=\"Verdana\"]\n")

            temp = self.inicio
            conteo = 0

            while True:
                archivo.write("\"node")
                archivo.write(str(conteo))
                archivo.write("\"[label = \"{<f0> |<f1> ")
                archivo.write(temp.nombre)
                archivo.write("|<f2>}\"];\n")

                if temp == self.fin:
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f2 -> \"node0\":f0;\n")                    
                else:
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f2 -> \"node")
                    conteo = conteo + 1
                    archivo.write(str(conteo))
                    archivo.write("\":f0;\n")
                    conteo = conteo - 1

                if temp == self.inicio:
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f0 -> \"node")    
                    num = self.longitud - 1                
                    archivo.write(str(num))
                    archivo.write("\":f2;\n")
                    
                else:
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f0 -> \"node")
                    conteo = conteo - 1
                    archivo.write(str(conteo))
                    archivo.write("\":f2;\n")
                    conteo = conteo + 1

                temp = temp.siguiente
                conteo = conteo + 1

                if temp == self.inicio:
                    break

            archivo.write("}")
            archivo.close()

            os.system("dot -Tpng usuariosReporte.dot -o usuariosReporte.png")
            os.system("usuariosReporte.png")

    def retornar_longitud(self):
        return self.longitud