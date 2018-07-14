
import curses
from frame import Frame
from food import Food
from snake import Snake

class Game:
    def __init__(self, width:int, height:int,stdscr):
        curses.curs_set(0)
        stdscr.clear()     
        stdscr.nodelay(True)  
        self.__stdscr = stdscr
        self.__width = width
        self.__height = height
        self.__frame = Frame(width, height,"*",stdscr)
        self.__food = Food(width//4,height//4,"$",stdscr,1,1,width-1,height -1)
        self.__snake = Snake(width//2, height//2,"+",stdscr)
        self.__total_time = 0
        self.__draw_time_buffer = 0
    
    def clear(self)->None:
        self.__frame = Frame( self.__width,  self.__height,"*", self.__stdscr)
        self.__food = Food( self.__width//4, self.__height//4,"$", self.__stdscr,1,1, self.__width-1, self.__height -1)
        self.__snake = Snake( self.__width//2,  self.__height//2,"+", self.__stdscr)

    def draw(self,time_delta:int)->None:
        self.__draw_time_buffer += time_delta
        if self.__draw_time_buffer > 30000:
            self.__draw_time_buffer -= 30000
            self.__stdscr.clear()
            self.__frame.draw()
            self.__food.draw()
            self.__snake.draw()
            self.__stdscr.refresh()

    def logic(self,time_delta:int)->None:       
        self.__total_time += time_delta   
        c = int(self.__stdscr.getch())
        self.__snake.turn(c)
        if self.__total_time > 200000:           
            self.__total_time -= 200000
            if self.__snake.is_hit_self() or self.__frame.is_hit(self.__snake.head):
                self.clear()
            if self.__snake.head.is_hit(self.__food):
                self.__snake.grow()
                self.__food.generate()
            self.__snake.move()