class Simulation:
    def __init__(self, ecs):
        self.ecs = ecs



    def get_render_data(self):
        return self.ecs.get_render_data()