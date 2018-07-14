import curses
import random
from datetime import timedelta, datetime

class Point:
    def __init__(self, x:int, y:int, symbol:str, stdscr)->None:
        self.__x = x
        self.__y = y
        self.__symbol = symbol
        self.__stdscr = stdscr

    @property
    def x(self)->int:
        return self.__x

    @x.setter
    def x(self, value:int):
        self.__x = value

    @property
    def y(self)->int:
        return self.__y

    @y.setter
    def y(self, value:int):
        self.__y = value

    def draw(self):
        self.__stdscr.addstr(self.__y,self.__x,self.__symbol)

    def is_hit(self, ather)->bool:
        return self.x == ather.x and self.y == ather.y


class Figure:

    def __init__(self):
        self._points:[Point] = []

    def draw(self)->None:
        for p in self._points:
            p.draw()

    def is_hit(self,point:Point)->bool:
        for p in self._points:
            if p.is_hit(point):
                return True
        return False

class Food(Point):

     def __init__(self, x:int, y:int, symbol:str, stdscr,minX:int, minY:int, maxX:int, maxY:int)->None:
         super().__init__(x,y,symbol,stdscr)
         self.__maxX = maxX
         self.__maxY = maxY
         self.__minY = minY
         self.__minX = minX

     def generate(self) -> None :
        self.x = random.randint(self.__minX,self.__maxX)
        self.y = random.randint(self.__minY, self.__maxY)

class Frame(Figure):

    def __init__(self, width:int, height:int, symbol:str,stdscr):
        super().__init__()
        for i in range(0, width):
            self._points.append(Point(i,0,symbol,stdscr))
            self._points.append(Point(i,height,symbol,stdscr))
        for i in range(0, height):
            self._points.append(Point(0,i,symbol,stdscr))
            self._points.append(Point(width,i,symbol,stdscr))
                



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

class Game:
    def __init__(self, width:int, height:int,stdscr):
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

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()     
    stdscr.nodelay(True)   
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




