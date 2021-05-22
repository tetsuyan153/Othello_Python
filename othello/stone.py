from enum import Enum

class Color(Enum):
    WHITE = "White"
    BLACK = "Black"

class Stone:

    def __init__(self, c):
        self._color = c
    
    @property
    def color(self):
        return self._color

    def reverse(self):
        if self._color == Color.BLACK:
            self._color = Color.WHITE
        else:
            self._color = Color.BLACK
    
    def __str__(self):
        return self._color.value

