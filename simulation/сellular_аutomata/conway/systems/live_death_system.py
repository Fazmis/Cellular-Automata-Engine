from simulation.сellular_аutomata.common import Position, State, NeighborFinder
from simulation.сellular_аutomata.common.base_systems import BaseSystem


class LifeDeathSystem(BaseSystem):
    def __init__(self, component_manager, neighbor_finder: NeighborFinder):
        super().__init__(component_manager)
        self.neighbor_finder = neighbor_finder

    def update(self):
        changes = []
        for position, state in self.component_manager.query(Position, State):
            alive_neighbors_count = len(self.neighbor_finder.get_alive_neighbors(position))
            new_value = (int(2 <= alive_neighbors_count <= 3) if state.value > 0
                         else int(alive_neighbors_count == 3))
            if new_value != state.value:
                changes.append((state, new_value))

        for component, value in changes:
            component.value = value