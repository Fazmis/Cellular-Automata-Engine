from simulation.сellular_аutomata.common.base_components import Position, IsAlive
from simulation.сellular_аutomata.common.base_systems import BaseSystem, NeighborSystem


class LifeDeathSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)
        self.neighbor_system = NeighborSystem(component_manager)

    def update(self):
        changes = []
        for position, alive in self.component_manager.query(Position, IsAlive):
            alive_neighbors_count = len(self.neighbor_system.get_alive_neighbors(position))
            new_state = (2 <= alive_neighbors_count <= 3 if alive.alive
                         else alive_neighbors_count == 3)
            if new_state != alive.alive:
                changes.append((alive, new_state))

        for component, value in changes:
            component.alive = value