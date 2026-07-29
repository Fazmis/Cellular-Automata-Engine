from enum import Enum, auto


class SimulationStates(Enum):
    NORMAL = auto()
    ALL_DIED = auto()
    STABLE = auto()
    CYCLED = auto()