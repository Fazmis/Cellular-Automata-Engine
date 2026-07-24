from .base_system import BaseSystem
from ..base_components import Position, IsAlive


class NeighborSystem(BaseSystem):
    def __init__(self, component_manager, radius=1):
        super().__init__(component_manager)
        self.radius = radius

    def get_alive_neighbors(self, position) -> list[int]:
        x, y = position.x, position.y
        alive_list = []
        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                if i == j == 0:
                    continue
                position_to_search = (x + i, y + j)
                components = self.component_manager.get_position_index(position_to_search)
                if components is None:
                    continue
                alive = components.get(IsAlive)
                if alive and alive.alive:
                    alive_list.append(alive.entity_id)

        return alive_list