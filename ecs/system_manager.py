from .systems import RenderSystem


class SystemManager:
    def __init__(self, ecs):
        self.component_manager = ecs.component_manager
        self.systems_to_update = []
        self.render_system = RenderSystem(self.component_manager)

    def add_system(self, system):
        activated_system = system(self.component_manager)
        self.systems_to_update.append(activated_system)

    def update(self, dt):
        for system in self.systems_to_update:
            system.update(dt)

    def get_render_data(self):
        return self.render_system.get_render_data()
