from simulation.сellular_аutomata.common import Position, IsAlive

class RenderSystem:
    def __init__(self, component_manager):
        self.component_manager = component_manager

    def get_render_data(self):
        render_data = self.component_manager.query(Position, IsAlive)
        return render_data

