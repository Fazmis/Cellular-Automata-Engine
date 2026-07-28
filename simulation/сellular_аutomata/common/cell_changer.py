from .base_components import IsAlive

class CellChanger:
    def __init__(self, component_manager):
        self.component_manager = component_manager

    def change_cell_alive_from_position(self, position: tuple[int, int]):
        alive = self.component_manager.get_position_index(position)[IsAlive]
        alive.alive = not alive.alive