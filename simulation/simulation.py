class Simulation:
    def __init__(self, ecs):
        self.ecs = ecs
        self.factory = None


    def initialize(self, factory, size=(20, 20), toroidal=True):
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