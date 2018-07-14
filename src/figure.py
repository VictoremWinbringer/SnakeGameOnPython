
from point import Point

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