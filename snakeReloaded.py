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

def snack_mas(stdscr,snake,h,w):
    snack1 = None

    while snack1 is None:
        posC1X = random.randint(4,w-4)
        posC1Y = random.randint(4,h-4)
        snack1 = [posC1Y,posC1X]        
        stdscr.addstr(posC1Y,posC1X,"+")

        if snake.toca_serpiente(posC1X,posC1Y) == True:            
            snakc1 = None
            
    return snack1

def snack_menos(stdscr,snake,h,w):
    snack2 = None
    
    while snack2 is None:
        posC2X = random.randint(4,w-4)
        posC2Y = random.randint(4,h-4)
        snack2 = [posC2Y, posC2X]
        stdscr.addstr(posC2Y,posC2X,"*")

        if snake.toca_serpiente(posC2X,posC2Y) == True:
            snack2  =  None

    return snack2

def score_panel(stdscr, score):
    h, w = stdscr.getmaxyx()
    scoreTexto =  "Score: {}".format(score.punteo_total())
    stdscr.addstr(2,w-20, scoreTexto)
    stdscr.refresh()

def juego(stdscr):
    snake = ListaDoble()    

    curses.curs_set(0)
    stdscr.nodelay(1)

    subir = False
    nivel = 1
    pasos = 0
    velocidad = 125
    stdscr.timeout(velocidad)

    h, w = stdscr.getmaxyx()
    ancho = w-3
    alto = h-3
    caja = [[3,3],[alto,ancho]]
    textpad.rectangle(stdscr,caja[0][0], caja[0][1], caja[1][0], caja[1][1])       

    snake.insertar_fin(w//3+1,h//3)
    snake.insertar_fin(w//3,h//3)
    snake.insertar_fin(w//3-1,h//3)

    direccion = curses.KEY_RIGHT

    snake.pintar_serpiente(stdscr)          
    comida1 = snack_mas(stdscr,snake,h,w)
    comida2 = snack_menos(stdscr,snake,h,w)
    score = Pila()
    stdscr.addstr(2,w//2-len("Snake Reloaded"), "Snake Reloaded")
    score_panel(stdscr,score)
    
    while 1:
        key = stdscr.getch()    
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direccion = key
        
        headx = snake.retornar_inicioX()
        heady = snake.retornar_inicioY()

        if direccion == curses.KEY_RIGHT:
            nuevo_inicio =  [heady, headx+1]
        elif direccion == curses.KEY_DOWN:
            nuevo_inicio =  [heady+1, headx]
        elif direccion == curses.KEY_UP:
            nuevo_inicio =  [heady-1, headx]
        elif direccion == curses.KEY_LEFT:
            nuevo_inicio =  [heady, headx-1]        

        snake.insertar_inicio(nuevo_inicio[1],nuevo_inicio[0])        
        stdscr.addstr(snake.retornar_inicioY(),snake.retornar_inicioX(),'S')
        
        if snake.comer(comida1[1],comida1[0]) == True:
            comida1 = snack_mas(stdscr,snake,h,w) 
            score.push(comida1[1],comida1[0])

        else:
            stdscr.addstr(snake.retornar_finY(), snake.retornar_finX()," ")
            snake.eliminar_fin()                        
        
        if snake.comer(comida2[1],comida2[0]) == True:
            comida2 = snack_menos(stdscr,snake,h,w)
            if snake.mostra_longitud() > 3:
                stdscr.addstr(snake.retornar_finY(), snake.retornar_finX()," ")
                score.pop()
                snake.eliminar_fin()     
                
        score_panel(stdscr,score)                  
        
        if score.punteo_total() != 0:
            if score.punteo_total()%15 == 0:            
                pasos = pasos + 1
            else:
                pasos = 0

        if pasos == 1:
            subir = True
        else:
            subir = False

        if subir == True:
            if velocidad > 5:
                velocidad = velocidad - 30
                stdscr.timeout(velocidad)


        if (snake.retornar_inicioX() == 3 or 
        snake.retornar_inicioY()== 3 or 
        snake.retornar_inicioX() == w-3 or
        snake.retornar_inicioY() == h-3 or
        snake.valores_repetidos() == True):
            stdscr.addstr(h//2,w//2-len("Game Over")//2,"Game Over")
            stdscr.nodelay(0)
            stdscr.getch()
            snake.graficar()
            score.graficar()
            time.sleep(5)            
            
            break


        stdscr.refresh()                  
  


curses.wrapper(juego)