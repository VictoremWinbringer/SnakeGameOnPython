
from figure import Figure
from point import Point

class Frame(Figure):

    def __init__(self, width:int, height:int, symbol:str,stdscr):
        super().__init__()
        for i in range(0, width):
            self._points.append(Point(i,0,symbol,stdscr))
            self._points.append(Point(i,height,symbol,stdscr))
        for i in range(0, height):
            self._points.append(Point(0,i,symbol,stdscr))
            self._points.append(Point(width,i,symbol,stdscr))