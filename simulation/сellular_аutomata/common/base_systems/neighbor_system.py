from .base_system import BaseSystem


class NeighborSystem(BaseSystem):
    def __init__(self, component_manager, radius=1):
        super().__init__(component_manager)
