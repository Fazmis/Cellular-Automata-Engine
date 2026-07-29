from copy import deepcopy
from .history_step import Step
from .simulation_states import SimulationStates
from ..сellular_аutomata.common import State


class History:
    def __init__(self, component_manager, snapshot_components:list):
        self.component_manager = component_manager
        self.snapshot_components = snapshot_components
        self._current_step = 0
        self.steps: dict[int, Step] = {}
        self.hashes: set[int] = set()
        self.state = SimulationStates.NORMAL

    def get_current_step(self) -> int:
        return self._current_step

    def get_state(self):
        return self.state

    def save(self):
        # snapshot
        snapshot = self._create_snapshot()
        # hash
        snapshot_hash = self._hash(snapshot)
        # state
        self._state_update(snapshot_hash)
        #save
        step_id = self._current_step
        self._current_step += 1
        self.steps[step_id] = Step(snapshot, snapshot_hash)
        self.hashes.add(snapshot_hash)

    def load(self, snapshot):
        for component_type, saves in snapshot.items():
            for save in saves:
                component = self.component_manager.component_entities[component_type][save.entity_id]
                for slot in save.__slots__:
                    setattr(component, slot, getattr(save, slot))

    def undo(self):
        if self._current_step <= 0:
            return
        self._current_step -= 1
        step_id = self._current_step
        step = self.steps.pop(step_id)
        self.hashes.discard(step.hash)
        self.load(step.snapshot)

    def _create_snapshot(self):
        snapshot = {}
        for component_type in self.snapshot_components:
            component_type_saves = []
            components = self.component_manager.query(component_type)
            for component in components:
                component_type_saves.append(deepcopy(component))
            snapshot[component_type] = component_type_saves
        return snapshot

    def _hash(self, snapshot):
        hash_step = []
        for key, values in snapshot.items():
            hash_values = tuple((v.entity_id, v.value) for v in sorted(values, key=lambda x: x.entity_id))
            hash_step.append(tuple((key, hash_values)))
        return hash(tuple(hash_step))

    def _state_update(self, snapshot_hash):

        def is_all_die():
            states = self.component_manager.query(State)
            return all(state.value <= 0 for state in states)

        if self._current_step <= 0:
            return
        last_step_hash = self.steps.get(self._current_step - 1).hash
        if is_all_die():
            self.state = SimulationStates.ALL_DIED
            self.hashes = set()
        elif snapshot_hash == last_step_hash:
            self.state = SimulationStates.STABLE
            self.hashes = set()
        elif snapshot_hash in self.hashes:
            self.state = SimulationStates.CYCLED
        else:
            self.state = SimulationStates.NORMAL
