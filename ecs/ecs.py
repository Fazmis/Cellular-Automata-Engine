from ecs.entity_manager import EntityManager
from ecs.component_manager import ComponentManager
from ecs.system_manager import SystemManager


class Ecs:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.component_manager = ComponentManager()
        self.system_manager = SystemManager(self)

    def update(self):
        self.system_manager.update()

    def add_entity(self, components: set|list):
        entity_id = self.entity_manager.create_entity()
        self.component_manager.add_entity(entity_id, components)

    def add_system(self, system):
        self.system_manager.add_system(system)

    def get_render_data(self):
        return self.system_manager.get_render_data()
