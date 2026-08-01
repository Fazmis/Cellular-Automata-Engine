from simulation.сellular_аutomata.common.base_components import Position, State


class NeighborFinder:
    def __init__(self, component_manager, grid_size: tuple[int, int], radius=1, toroidal=True):
        self.component_manager = component_manager
        self.grid_size = grid_size
        self.radius = radius
        self.toroidal = toroidal

    def _toroidal_next_pos(self, x, y, i, j) -> tuple[int, int]:
        return (
            (x + i + self.grid_size[0]) % self.grid_size[0],
            (y + j + self.grid_size[1]) % self.grid_size[1]
        )

    @staticmethod
    def _next_pos(x, y, i, j) -> tuple[int, int]:
        return (
                x + i,
                y + j
            )

    def get_neighbor_states(self, position: Position) -> list[int]:
        x, y = position.x, position.y
        if self.toroidal:
            next_pos = self._toroidal_next_pos
        else:
            next_pos = self._next_pos
        neighbor_states = []
        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                if i == j == 0:
                    continue
                position_to_search = next_pos(x, y, i, j)
                components = self.component_manager.get_position_index(position_to_search)
                if components is None:
                    continue
                state = components.get(State)
                neighbor_states.append(state.value)

        return neighbor_states

    def count_neighbors(self, position, predicate) -> int:
        states = self.get_neighbor_states(position)
        return sum(predicate(state) for state in states)

    def count_neighbors_equal(self, position, value) -> int:
        return self.count_neighbors(
            position,
            lambda x: x == value
        )

    def count_neighbors_greater(self, position, value) -> int:
        return self.count_neighbors(
            position,
            lambda x: x > value
        )

    def count_neighbors_less(self, position, value) -> int:
        return self.count_neighbors(
            position,
            lambda x: x < value
        )
