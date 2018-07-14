
import random
from point import Point

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