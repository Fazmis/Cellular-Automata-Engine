from .utils import CellEditor, History, SimulationStates
from .сellular_аutomata.common.base_components import Position, State
from .сellular_аutomata.factories import BinaryFactory


class Simulation:
    def __init__(self, ecs) -> None:
        self.ecs = ecs
        self.size = None
        self.factory: BinaryFactory | None = None
        self.cell_editor = CellEditor(self.ecs.component_manager)
        self.history = History(self.ecs.component_manager, [State])

    def initialize(self, automaton_preset, size=(20, 20), toroidal=True) -> None:
        self.size = size
        self.factory = BinaryFactory(self.ecs.component_manager, size, automaton_preset, toroidal)

        for system in self.factory.get_systems():
            self.ecs.add_system(system)

        width, height = size
        for x in range(width):
            for y in range(height):
                cell = self.factory.default_entity(position=(x, y))
                self.ecs.add_entity(cell)

    def _get_ecs_render_data(self) -> list[tuple[tuple, int]]:
        query = self.ecs.component_manager.query(Position, State)
        render_data = []
        for position, state in query:
            render_data.append((
                (position.x, position.y),
                state.value
            ))
        return render_data

    def get_render_data(self) -> dict:
        render_data = {}

        title = self.factory.get_display_config()
        generation_step = self.history.get_current_step()
        ecs_render_data = self._get_ecs_render_data()
        display_config = self.factory.get_display_config()
        state = self.history.get_state()
        match state:
            case SimulationStates.NORMAL:
                state = "Running"
            case SimulationStates.ALL_DIED:
                state = "No living cells!"
            case SimulationStates.STABLE:
                state = "Stable configuration"
            case SimulationStates.CYCLED:
                state = "Loop detected"
        render_data["title"] = title
        render_data["generation_step"] = generation_step
        render_data["grid"] = ecs_render_data
        render_data["display_config"] = display_config
        render_data["state"] = state
        return render_data

    def change_cell(self, position: tuple[int, int]):
        position = (
            position[0] % self.size[0],
            position[1] % self.size[1],
                    )
        self.cell_editor.change_cell_state_from_position(position)

    def next_step(self) -> None:
        self.history.save()
        self.ecs.update()

    def previous_step(self) -> None:
        self.history.undo()
