import curses
from curses import textpad
from snakeReloaded import *

game = snakeGame()

menu = ["1. Play", "2. Scoreboard", "3. User Selection", "4. Reports", "5. Bulk Loading", "6. Exit"]

def mostrar_menu(stdscr, selected_row_idx):
    stdscr.clear()
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

def main(stdscr):    
    curses.curs_set(0)

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
                game.juego(stdscr)                 
                main(stdscr)
            if current_row == 1:
                break
            if current_row == 2:
                break
            if current_row == 3:
                break
            if current_row == 4:
                break
            if current_row == 5:
                break

        mostrar_menu(stdscr, current_row)

curses.wrapper(main)