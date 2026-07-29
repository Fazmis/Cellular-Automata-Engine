from ..common import Position, State, NeighborFinder, AutomataConfig
from .systems import LifeDeathSystem
from ..common.base_components import BaseComponent


class Factory:
    def __init__(self, component_manager, size:tuple[int, int], toroidal:bool):
        self.title = "Conway Game Of Life"
        self.component_manager = component_manager
        self.size = size
        self.toroidal = toroidal
        self.neighbor_finder = NeighborFinder(self.component_manager, size, toroidal)
        self.cell_states_count = 2
        self.config = AutomataConfig(
            states_count = self.cell_states_count,
            symbols = {
                0: " ",
                1: "█",
            }
        )

        self.components = [
            Position,
            State,
        ]

        self.systems = [
            LifeDeathSystem(self.component_manager, self.neighbor_finder)
        ]

    def get_config(self) -> AutomataConfig:
        return self.config

    def get_components(self):
        return self.components

    def get_systems(self):
        return self.systems

    def default_entity(self, position: tuple[int, int] = (0, 0)) -> list:
        x, y = position
        entity = [
            Position(x, y),
            State(self.cell_states_count)
        ]
        return entity