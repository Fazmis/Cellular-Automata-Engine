class SystemManager:
    def __init__(self, ecs):
        self.component_manager = ecs.component_manager
        self.systems_to_update = []

    def add_system(self, system):
        self.systems_to_update.append(system)

    def update(self):
        for system in self.systems_to_update:
            system.update()

