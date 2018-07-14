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