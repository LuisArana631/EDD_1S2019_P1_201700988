import curses
import random
import time
from curses import textpad
from curses import KEY_RIGHT
from curses import KEY_LEFT
from curses import KEY_UP
from curses import KEY_DOWN
from curses import KEY_BACKSPACE
from listaDoble import *
from pila import *
from fila import  *

class snakeGame:

    def __init__(self):
        self.subir = False
        self.nivel = 1
        self.pasos = 0
        self.velocidad = 125
        self.snake = ListaDoble()
        self.score = Pila()
        self.top = Fila()


    def snack_mas(self,stdscr,snake,h,w):
        snack1 = None

        while snack1 is None:
            posC1X = random.randint(4,w-4)
            posC1Y = random.randint(4,h-4)
            snack1 = [posC1Y,posC1X]        
            stdscr.addstr(posC1Y,posC1X,"+")

            if self.snake.toca_serpiente(posC1X,posC1Y) == True:            
                snakc1 = None
                
        return snack1

    def snack_menos(self,stdscr,snake,h,w):
        snack2 = None
        
        while snack2 is None:
            posC2X = random.randint(4,w-4)
            posC2Y = random.randint(4,h-4)
            snack2 = [posC2Y, posC2X]
            stdscr.addstr(posC2Y,posC2X,"*")

            if self.snake.toca_serpiente(posC2X,posC2Y) == True:
                snack2  =  None

        return snack2

    def score_panel(self,stdscr, score):
        h, w = stdscr.getmaxyx()
        scoreTexto =  "Score: {}".format(score.punteo_total())
        stdscr.addstr(2,w-10, scoreTexto)
        stdscr.refresh()

    def mostrar_top(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(0)
        stdscr.clear()

        h, w = stdscr.getmaxyx()
        ancho = w-3
        alto = h-3
        caja = [[3,3],[alto,ancho]]
        textpad.rectangle(stdscr,caja[0][0], caja[0][1], caja[1][0], caja[1][1]) 
        stdscr.addstr(2,w//2-7, "Snake Reloaded")
        stdscr.refresh()
        if self.top.fila_vacia() != True:
            self.top.pintar_top(stdscr,w)                        
        else:
            stdscr.addstr(h//2,w//2-5, "No hay registro de juegos")            
        stdscr.getch()

    def juego(self,stdscr,usuario): 

        self.snake.reiniciar_snake()        
        self.score.reiniciar_pila()
        self.subir = False
        self.nivel = 1
        self.pasos = 0
        self.velocidad = 125

        curses.curs_set(0)
        stdscr.nodelay(1)
        
        stdscr.timeout(self.velocidad)

        h, w = stdscr.getmaxyx()
        ancho = w-3
        alto = h-3
        caja = [[3,3],[alto,ancho]]
        textpad.rectangle(stdscr,caja[0][0], caja[0][1], caja[1][0], caja[1][1])       

        self.snake.insertar_fin(w//3+1,h//3)
        self.snake.insertar_fin(w//3,h//3)
        self.snake.insertar_fin(w//3-1,h//3)

        direccion = curses.KEY_RIGHT

        self.snake.pintar_serpiente(stdscr)                  
        comida1 = self.snack_mas(stdscr,self.snake,h,w)
        comida2 = self.snack_menos(stdscr,self.snake,h,w)
        stdscr.addstr(2,w//2-7, "Snake Reloaded")
        self.score_panel(stdscr,self.score)
        stdscr.addstr(2,3,usuario)
        
        while 1:
            key = stdscr.getch()    
            if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
                direccion = key
            
            headx = self.snake.retornar_inicioX()
            heady = self.snake.retornar_inicioY()

            if direccion == curses.KEY_RIGHT:
                nuevo_inicio =  [heady, headx+1]
            elif direccion == curses.KEY_DOWN:
                nuevo_inicio =  [heady+1, headx]
            elif direccion == curses.KEY_UP:
                nuevo_inicio =  [heady-1, headx]
            elif direccion == curses.KEY_LEFT:
                nuevo_inicio =  [heady, headx-1]        

            self.snake.insertar_inicio(nuevo_inicio[1],nuevo_inicio[0])        
            stdscr.addstr(self.snake.retornar_inicioY(),self.snake.retornar_inicioX(),'S')
            
            if self.snake.comer(comida1[1],comida1[0]) == True:
                comida1 = self.snack_mas(stdscr,self.snake,h,w) 
                self.score.push(comida1[1],comida1[0])

            else:
                stdscr.addstr(self.snake.retornar_finY(), self.snake.retornar_finX()," ")
                self.snake.eliminar_fin()                        
            
            if self.snake.comer(comida2[1],comida2[0]) == True:
                comida2 = self.snack_menos(stdscr,self.snake,h,w)
                if self.snake.mostra_longitud() > 3:
                    stdscr.addstr(self.snake.retornar_finY(), self.snake.retornar_finX()," ")
                    self.score.pop()
                    self.snake.eliminar_fin()     
                    
            self.score_panel(stdscr,self.score)                  
            
            if self.score.punteo_total() != 0:
                if self.score.punteo_total()%15 == 0:            
                    self.pasos = self.pasos + 1
                else:
                    self.pasos = 0

            if self.pasos == 1:
                self.subir = True
            else:
                self.subir = False

            if self.subir == True:
                if self.velocidad > 5:
                    self.velocidad = self.velocidad - 30
                    stdscr.timeout(self.velocidad)


            if (self.snake.retornar_inicioX() == 3 or 
            self.snake.retornar_inicioY()== 3 or 
            self.snake.retornar_inicioX() == w-3 or
            self.snake.retornar_inicioY() == h-3 or
            self.snake.valores_repetidos() == True):
                self.top.insertar(usuario,self.score.punteo_total())
                if self.top.retornar_long() > 10:
                    self.top.eliminar()            
                stdscr.addstr(h//2,w//2-len("Game Over")//2,"Game Over")
                stdscr.nodelay(0)
                stdscr.getch()                 
                time.sleep(1)                     
                break
            stdscr.refresh()                            

    def imprimir_reportes(self):
        self.snake.graficar()
        self.top.graficar()
        self.score.graficar()

