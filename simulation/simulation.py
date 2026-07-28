from .сellular_аutomata.common import CellChanger


class Simulation:
    def __init__(self, ecs):
        self.ecs = ecs
        self.size = None
        self.factory = None
        self.cell_changer = CellChanger(ecs.component_manager)


    def initialize(self, factory, size=(20, 20), toroidal=True):
        self.size = size
        self.factory = factory(self.ecs.component_manager, size, toroidal)

        for system in self.factory.get_systems():
            self.ecs.add_system(system)

        width, height = size
        for x in range(width):
            for y in range(height):
                cell = self.factory.default_entity(position=(x, y))
                self.ecs.add_entity(cell)


    def get_render_data(self):
        return self.ecs.get_render_data()

    def change_cell(self, position: tuple[int, int]):
        position = (
            position[0] % self.size[0],
            position[1] % self.size[1],
                    )
        self.cell_changer.change_cell_alive_from_position(position)

    def next_step(self):
        self.ecs.update()