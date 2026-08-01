from ..common.base_components import Position, State
from ..common.base_systems import BirthSurviveSystem
from ..common.base_configs import AutomatonPreset, DisplayAutomatonConfig
from ..common.utils import NeighborFinder


class BinaryFactory:
    def __init__(self, component_manager, size: tuple[int, int], automaton_preset: AutomatonPreset, toroidal: bool):
        self.component_manager = component_manager
        self.size = size
        self.automaton_preset = automaton_preset
        self.toroidal = toroidal
        self.neighbor_finder = NeighborFinder(self.component_manager, size, toroidal)

        self.cell_states_count = 2

        self.components = [
            Position,
            State,
        ]

        self.systems = [
            BirthSurviveSystem(
                self.component_manager,
                self.neighbor_finder,
                self.automaton_preset.binary_automata_config.birth,
                self.automaton_preset.binary_automata_config.survive,
            )
        ]

    def get_display_config(self) -> DisplayAutomatonConfig:
        return self.automaton_preset.display_automata_config

    def get_components(self) -> list[object]:
        return self.components

    def get_systems(self) -> list[object]:
        return self.systems

    def default_entity(self, position: tuple[int, int] = (0, 0)) -> list:
        x, y = position
        entity = [
            Position(x, y),
            State(self.cell_states_count)
        ]
        return entity
