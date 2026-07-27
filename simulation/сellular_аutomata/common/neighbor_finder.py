from simulation.сellular_аutomata.common.base_components import Position, IsAlive


class NeighborFinder:
    def __init__(self, component_manager, grid_size: tuple[int, int], radius=1, toroidal=True):
        self.component_manager = component_manager
        self.grid_size = grid_size
        self.radius = radius
        self.toroidal = toroidal

    def get_alive_neighbors(self, position: Position) -> list[int]:
        x, y = position.x, position.y
        if self.toroidal:
            next_pos = lambda i, j: (
                (x + i + self.grid_size[0]) % self.grid_size[0],
                (y + j + self.grid_size[1]) % self.grid_size[1]
            )
        else:
            next_pos = lambda i, j: (
                x + i,
                y + j
            )
        alive_list = []
        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                if i == j == 0:
                    continue
                position_to_search = next_pos(i, j)
                components = self.component_manager.get_position_index(position_to_search)
                if components is None:
                    continue
                alive = components.get(IsAlive)
                if alive and alive.alive:
                    alive_list.append(alive.entity_id)

        return alive_list