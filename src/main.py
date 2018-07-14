from datetime import timedelta, datetime
from game import Game
import curses

def main(stdscr): 
    game = Game(30,10, stdscr)
    now = datetime.now()
    while True:
        new_now = datetime.now()
        time_delta = new_now - now
        now = new_now       
        game.logic(time_delta.microseconds)
        game.draw(time_delta.microseconds) 

if __name__ == '__main__':
    curses.wrapper(main)




