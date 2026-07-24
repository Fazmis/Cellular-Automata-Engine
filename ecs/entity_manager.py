class EntityManager:
    def __init__(self):
        self._next_id = 0
        self.entities = set()

    def create_entity(self):
        entity_id = self._next_id
        self._next_id += 1
        self.entities.add(entity_id)
        return entity_id
