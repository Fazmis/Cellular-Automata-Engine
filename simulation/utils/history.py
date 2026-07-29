from copy import deepcopy


class History:
    def __init__(self, component_manager, snapshot_components:list):
        self.component_manager = component_manager
        self._current_step = 0
        self.steps: dict[int, dict] = {}
        self.snapshot_components = snapshot_components

    def save(self):
        snapshot = {}
        for component_type in self.snapshot_components:
            component_type_saves = []
            components = self.component_manager.query(component_type)
            for component in components:
                component_type_saves.append(deepcopy(component))
            snapshot[component_type] = component_type_saves
        step_id = self._current_step
        self._current_step += 1
        self.steps[step_id] = snapshot

    def undo(self):
        if self._current_step <= 0:
            return
        self._current_step -= 1
        step = self._current_step
        snapshot = self.steps.pop(step)
        self.load(snapshot)

    def load(self, snapshot):
        for component_type, saves in snapshot.items():
            for save in saves:
                component = self.component_manager.component_entities[component_type][save.entity_id]
                for slot in save.__slots__:
                    setattr(component, slot, getattr(save, slot))