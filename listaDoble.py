import os

class Nodo:
    def __init__(self, posX=None, posY=None):
        self.posX = posX
        self.posY = posY
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.longitud = 0

    def lista_vacia(self):
        return self.inicio == None

    def insertar_inicio(self, posX, posY):
        nuevo = Nodo(posX, posY)
        if self.lista_vacia() == True:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo
        self.longitud = self.longitud + 1
    
    def insertar_fin(self, posX, posY):
        nuevo = Nodo(posX, posY)
        if self.lista_vacia() == True:
            self.inicio = nuevo
            self.fin =  nuevo
        else:
            nuevo.anterior = self.fin
            self.fin.siguiente = nuevo
            self.fin = nuevo
        self.longitud = self.longitud + 1

    def eliminar_inicio(self):
        if self.lista_vacia() != True:
            aux = self.inicio.siguiente
            aux.anterior = None
            self.inicio.siguiente = None
            self.inicio = aux
        self.longitud = self.longitud - 1

    def eliminar_fin(self):
        if self.lista_vacia() != True:
            aux = self.fin.anterior
            aux.siguiente = None
            self.fin.anterior = None
            self.fin = aux
        self.longitud = self.longitud - 1

    def graficar(self):
        if self.lista_vacia() == True:
            print("Esta vacia la lista")
        else:
            archivo = open("serpienteReporte.dot","w")
            archivo.write("digraph serpiente {\n")
            archivo.write("label=\"Posicion de la serpiente\";\n")
            archivo.write("rankdir=LR\n")
            archivo.write("graph [fontsize=20 fontname=\"Verdana\" compound=true];\n")
            archivo.write("node [shape=record fontsize=20 fontname=\"Verdana\"]\n")

            temp = self.inicio
            conteo = 0  
                   
            while temp is not None:
                archivo.write("\"node")
                archivo.write(str(conteo))
                archivo.write("\"[label = \"{<f0> |<f1> (")
                archivo.write(str(temp.posX))
                archivo.write(",")
                archivo.write(str(temp.posY))
                archivo.write(")|<f2>}\"];\n")               
                    
                if temp.siguiente is not None:
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f2 ->\"node")
                    conteo = conteo + 1
                    archivo.write(str(conteo))
                    archivo.write("\":f0;\n")
                    conteo = conteo - 1                     
                else:                    
                    archivo.write("nodenullfin[label = \"<f0> null\"];\n")
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f2 -> \"nodenullfin\":f0;\n")                                
                    
                
                if temp.anterior is not None:                                                            
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f0 -> \"node")
                    conteo = conteo - 1
                    archivo.write(str(conteo))
                    archivo.write("\":f2;\n")
                    conteo = conteo + 1                    
                else:                    
                    archivo.write("nodenullinicio[label = \"<f0> null\"];\n")
                    archivo.write("\"node")
                    archivo.write(str(conteo))
                    archivo.write("\":f0 -> \"nodenullinicio\":f0;\n")

                temp = temp.siguiente   
                conteo = conteo + 1                             

            archivo.write("}")
            archivo.close()

            os.system("dot -Tpng serpienteReporte.dot -o serpienteReporte.png")
            os.system("serpienteReporte.png")

    def mostrar_lista_doble(self):
        if self.lista_vacia() == True:
            print("Lista doble vacia")
        else:
            temp = self.inicio
            while temp is not None:
                print(temp.posX,",",temp.posY,"|")
                temp = temp.siguiente

    
