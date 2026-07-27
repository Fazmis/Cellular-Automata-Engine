from simulation.сellular_аutomata.common import Position, IsAlive

class RenderSystem:
    def __init__(self, component_manager):
        self.component_manager = component_manager

    def get_render_data(self):
        query = self.component_manager.query(Position, IsAlive)
        render_data = []
        for position, isalive in query:
            render_data.append((
                (position.x, position.y),
                isalive.alive
            ))
        return render_data
