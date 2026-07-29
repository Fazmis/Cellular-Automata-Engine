from enum import Enum, auto


class Command(Enum):
    EXIT = auto()
    EDIT_CELL = auto()
    NEXT_STEP = auto()
    PREVIOUS_STEP = auto()
