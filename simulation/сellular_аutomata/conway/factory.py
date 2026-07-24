from ..common.base_components import Position, IsAlive
from systems import LifeDeathSystem
class Factory:
    def __init__(self):
        self.components = [
            Position,
            IsAlive,
        ]

        self.systems = [
            LifeDeathSystem
        ]

    def get_components(self):
        return self.components

    def get_systems(self):
        return self.systems
