from ..common import Position, IsAlive, NeighborFinder
from .systems import LifeDeathSystem
class Factory:
    def __init__(self, component_manager, size:tuple[int, int], toroidal:bool):
        self.component_manager = component_manager
        self.size = size
        self.toroidal = toroidal
        self.neighbor_finder = NeighborFinder(self.component_manager, size, toroidal)

        self.components = [
            Position,
            IsAlive,
        ]

        self.systems = [
            LifeDeathSystem(self.component_manager, self.neighbor_finder)
        ]

    def get_components(self):
        return self.components

    def get_systems(self):
        return self.systems

    def default_entity(self, position: tuple[int, int] = (0, 0)) -> list:
        x, y = position
        entity = [
            Position(x, y),
            IsAlive()
        ]
        return entity