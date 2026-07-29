from simulation.сellular_аutomata.common import State

class CellEditor:
    def __init__(self, component_manager):
        self.component_manager = component_manager

    def change_cell_state_from_position(self, position: tuple[int, int]):
        state = self.component_manager.get_position_index(position)[State]
        state.value = (state.value + 1) % state.max_value