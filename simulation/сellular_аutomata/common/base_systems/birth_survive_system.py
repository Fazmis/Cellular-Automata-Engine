from ..base_components import Position, State
from .base_system import BaseSystem
from ..neighbor_finder import NeighborFinder


class BirthSurviveSystem(BaseSystem):
    def __init__(self, component_manager, neighbor_finder: NeighborFinder, birth: set[int], survive: set[int]):
        super().__init__(component_manager)
        self.neighbor_finder = neighbor_finder
        self.birth_counts = birth
        self.survive_counts = survive

    def update(self):
        changes = []
        for position, state in self.component_manager.query(Position, State):
            alive_count = self.neighbor_finder.count_neighbors_greater(position, 0)
            if state.value > 0:
                new_state_value = int(alive_count in self.survive_counts)
            else:
                new_state_value = int(alive_count in self.birth_counts)
            if state.value != new_state_value:
                changes.append([state, new_state_value])

        for component, value in changes:
            component.value = value