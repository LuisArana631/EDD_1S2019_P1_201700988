import curses
from curses import textpad
from curses.textpad import Textbox, rectangle
from curses import KEY_UP
from curses import KEY_DOWN
from curses import KEY_ENTER
import snakeReloaded
from snakeReloaded import *
import listaDobleCircular
from listaDobleCircular import *

game = snakeGame()
usuarios = ListaDobleCircular()

menu = ["1. Play", "2. Scoreboard", "3. User Selection", "4. Reports", "5. Bulk Loading"]

def mostrar_menu(stdscr, selected_row_idx):
    stdscr.clear()
    stdscr.nodelay(0)
    h, w = stdscr.getmaxyx()
    ancho = w-3
    alto = h-3
    caja = [[3,3],[alto,ancho]]
    textpad.rectangle(stdscr,caja[0][0], caja[0][1], caja[1][0], caja[1][1]) 
    stdscr.addstr(2,w//2-7, "Snake Reloaded")
    stdscr.refresh()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def ingresar_usuario(stdscr):
    stdscr.clear()
    stdscr.nodelay(0)
    h, w = stdscr.getmaxyx()
    ancho = w-3
    alto = h-3
    caja = [[3,3],[alto,ancho]]
    textpad.rectangle(stdscr,caja[0][0], caja[0][1], caja[1][0], caja[1][1]) 
    stdscr.addstr(2,w//2-7, "Snake Reloaded")
    stdscr.addstr(6,w//2-9,"Ingresa tu nickname")
    stdscr.refresh() 
    
    editwin = curses.newwin(1,20, 10,50)
    stdscr.refresh()
    box = Textbox(editwin)
    box.edit()
    usuario_selected = box.gather()    
    editwin.clear()    

    print(usuario_selected) 
    return usuario_selected    

def bulk_usuarios(stdscr):
    stdscr.clear()
    stdscr.nodelay(0)
    h, w = stdscr.getmaxyx()
    ancho = w-3
    alto = h-3
    caja = [[3,3],[alto,ancho]]
    textpad.rectangle(stdscr,caja[0][0], caja[0][1], caja[1][0], caja[1][1]) 
    stdscr.addstr(2,w//2-7, "Snake Reloaded")
    stdscr.addstr(6,w//2-16,"Ingresa la direccion del archivo")
    stdscr.refresh() 
    
    editwin = curses.newwin(1,90, 10,20)
    stdscr.refresh()
    box = Textbox(editwin)
    box.edit()
    direccion = box.gather()    
    editwin.clear()
    
    try:
        archivo = open(direccion,"r")     
        conteo = 0       
        
        for linea in archivo.readlines():
            if conteo != 0:            
                usuarios.insertar(linea)
            conteo = conteo + 1

        archivo.close()
    except:
        stdscr.addstr(h//2,w//2,"El archivo no se encuentra")
        time.sleep(2)

def seleccionar_usuario(stdscr):
    stdscr.clear()
    stdscr.nodelay(0)
    h, w = stdscr.getmaxyx()
    ancho = w-3
    alto = h-3
    caja = [[3,3],[alto,ancho]]
    textpad.rectangle(stdscr,caja[0][0], caja[0][1], caja[1][0], caja[1][1]) 
    stdscr.addstr(2,w//2-7, "Snake Reloaded")
    stdscr.addstr(6,w//2-16,"Ingresa la direccion del archivo")
    stdscr.addstr(h//2,5,"<-")
    stdscr.addstr(h//2,w-5,"->")
    stdscr.refresh() 
    stdscr.getch()

def main(stdscr):  
    usuario_selected = ""
    stdscr = curses.initscr()      
    curses.curs_set(0)
    stdscr.nodelay(0)                

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    current_row = 0
    mostrar_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()             

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:            
            if current_row == 0:                                
                stdscr.clear()
                curses.noecho()

                if usuario_selected == "": 
                    stdscr.nodelay(0)       
                    curses.noecho()        
                    curses.flushinp()                        
                    usuario_selected = ingresar_usuario(stdscr)
                    curses.noecho()
                    stdscr.clear()

                curses.noecho()
                game.juego(stdscr, usuario_selected)                            
            if current_row == 1:
                stdscr.clear()
                game.mostrar_top(stdscr)           
            if current_row == 2:
                seleccionar_usuario(stdscr)
            if current_row == 3:
                game.imprimir_reportes()
                usuarios.graficar()
            if current_row == 4:
                stdscr.clear()
                bulk_usuarios(stdscr)

        usuario_selected = ""
        stdscr.nodelay(0)
        mostrar_menu(stdscr, current_row)

curses.wrapper(main)