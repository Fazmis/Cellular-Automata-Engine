from simulation.components import Position, IsAlive

class RenderSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)

    def get_render_data(self):
        render_data = self.component_manager.query(Position, IsAlive)
        return render_data

