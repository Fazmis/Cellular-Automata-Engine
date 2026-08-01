from simulation.сellular_аutomata.common import Position, State


class NeighborFinder:
    def __init__(self, component_manager, grid_size: tuple[int, int], radius=1, toroidal=True):
        self.component_manager = component_manager
        self.grid_size = grid_size
        self.radius = radius
        self.toroidal = toroidal

    def get_neighbor_states(self, position: Position) -> list[int]:
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
        neighbor_states = []
        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                if i == j == 0:
                    continue
                position_to_search = next_pos(i, j)
                components = self.component_manager.get_position_index(position_to_search)
                if components is None:
                    continue
                state = components.get(State)
                neighbor_states.append(state.value)

        return neighbor_states

    def count_neighbors(self, position, predicate):
        states = self.get_neighbor_states(position)
        return sum(predicate(state) for state in states)

    def count_neighbors_equal(self, position, value):
        predicate = lambda x: x == value
        return self.count_neighbors(position, predicate)

    def count_neighbors_greater(self, position, value):
        predicate = lambda x: x > value
        return self.count_neighbors(position, predicate)

    def count_neighbors_less(self, position, value):
        predicate = lambda x: x < value
        return self.count_neighbors(position, predicate)
