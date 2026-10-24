from dataclasses import dataclass


@dataclass()
class Cursor:
    x: int = 0
    y: int = 0

    def __add__(self, other):
        if isinstance(other, tuple):
            if len(other) == 2:
                x, y = other
                self.x += x
                self.y += y
                return self
            else:
                raise ValueError("The length of the item being folded must be 2.")
        else:
            return NotImplemented
