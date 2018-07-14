
from figure import Figure
from point import Point
import curses

class Snake(Figure):

    def __init__(self, x:int, y:int, symbol:str,stdscr):
        super().__init__()
        self.__head = Point(x,y,symbol, stdscr)
        self.__symbol = symbol
        self.__stdscr = stdscr
        self.__dx = 1
        self.__dy = 0
        for i in range(1,3):
            self._points.append(Point(x-i,y-i,symbol,stdscr))

    def move(self)->None:
        x = self.__head.x
        y = self.__head.y        
        self.__head.y+=self.__dy
        self.__head.x+=self.__dx  
        for p in self._points:
            temp_x, temp_y = p.x, p.y
            p.x, p.y = x, y
            x, y = temp_x, temp_y          
            
    def is_hit_self(self)->bool:
        return self.is_hit(self.__head)

    @property
    def head(self)->Point:
        return self.__head

    def turn(self,direction:int)->None:
        c = int(direction)
        if c == curses.KEY_UP:
            self.__dy = -1
            self.__dx = 0     
        elif c == curses.KEY_DOWN:
            self.__dy = 1
            self.__dx = 0
        elif c == curses.KEY_LEFT:
            self.__dx = -1
            self.__dy = 0
        elif c == curses.KEY_RIGHT:
           self.__dx = 1 
           self.__dy = 0
    
    def grow(self):
        self._points.append(Point(1,1,self.__symbol, self.__stdscr))

    def draw(self):
        super().draw()
        self.__head.draw()