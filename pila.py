import os

class Nodo:
    def __init__(self, posX=None, posY=None):
        self.posX = posX
        self.posY = posY
        self.abajo = None

class Pila:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def pila_vacia(self):
        return self.cabeza == None

    def push(self, posX, posY):
        nuevo = Nodo(posX, posY)
        if self.pila_vacia() != True:            
            nuevo.abajo = self.cabeza
        self.cabeza = nuevo

    def pop(self):
        if self.pila_vacia() != True:
            temp = self.cabeza.abajo
            self.cabeza.abajo = None
            self.cabeza = temp
    
    def punteo_total(self):
        return self.longitud

    def graficar(self):
        if self.pila_vacia() ==  True:
            print("Esta vacia la pila")
        else:
            archivo = open("punteoReporte.dot", "w")
            archivo.write("digraph punteo {\n")
            archivo.write("label=\"Registro de Puntos\";\n")
            archivo.write("graph [fontsize=25 fontname=\"Verdana\" compound=true];\n")
            archivo.write("node [shape=record fontsize=25 fontname=\"Verdana\"]\n")
            
            archivo.write("struct1 [label=\"{<f0> |")
            temp = self.cabeza
            conteo = 1
            while temp is not None:
                if temp.abajo is None:
                    archivo.write("<f")
                    archivo.write(str(conteo))
                    archivo.write("> (")
                    archivo.write(str(temp.posX))
                    archivo.write(",")
                    archivo.write(str(temp.posY))
                    archivo.write(")}\"];")
                else:
                    archivo.write("<f")
                    archivo.write(str(conteo))
                    archivo.write("> (")
                    archivo.write(str(temp.posX))
                    archivo.write(",")
                    archivo.write(str(temp.posY))
                    archivo.write(")|")
                temp = temp.abajo
                conteo = conteo + 1            
            
            archivo.write("}")
            archivo.close()

            os.system("dot -Tpng punteoReporte.dot -o punteoReporte.png")
            os.system("punteoReporte.png")

    def mostrar_pila(self):
        if self.pila_vacia() ==  True:
            print("Esta vacia la pila")
        else:
            aux = self.cabeza
            while aux is not None:            
                print(str(aux.posX),",",str(aux.posY) , "|")
                aux = aux.abajo
