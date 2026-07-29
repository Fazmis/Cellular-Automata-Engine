from .utils import CellEditor, History
from .сellular_аutomata.common import Position, State


class Simulation:
    def __init__(self, ecs):
        self.ecs = ecs
        self.size = None
        self.factory = None
        self.cell_editor = CellEditor(self.ecs.component_manager)
        self.history = History(self.ecs.component_manager, [State])


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

    def _get_ecs_render_data(self):
        query = self.ecs.component_manager.query(Position, State)
        render_data = []
        for position, state in query:
            render_data.append((
                (position.x, position.y),
                state.value
            ))
        return render_data

    def get_render_data(self):
        render_data = {}

        ecs_render_data = self._get_ecs_render_data()
        config = self.factory.get_config()

        render_data["title"] = self.factory.title
        render_data["generation"] = self.history.get_current_step()
        render_data["grid"] = ecs_render_data
        render_data["grid_config"] = config
        return render_data


    def change_cell(self, position: tuple[int, int]):
        position = (
            position[0] % self.size[0],
            position[1] % self.size[1],
                    )
        self.cell_editor.change_cell_state_from_position(position)

    def next_step(self):
        self.history.save()
        self.ecs.update()

    def previous_step(self):
        self.history.undo()
