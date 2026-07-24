from simulation.сellular_аutomata.common.base_components.position import Position


class ComponentManager:
    def __init__(self):
        self.entity_components = {} # entity_id: (components)
        self.component_entities = {} # component_type: id: component_obj
        self.index_position_components = {} # (x, y): component_type: component_obj

    def add_entity(self, entity_id:int, components:list):
        self.entity_components[entity_id] = components
        for component in components:
            component.entity_id = entity_id
            self._add_component(component, entity_id)
        self._add_indexes(components)

    def _add_indexes(self, components):
        components_by_type = {
            type(component): component
            for component in components
        }
        if Position in components_by_type:
            position = components_by_type[Position]
            key = (position.x, position.y)
            self.index_position_components[key] = components_by_type

    def _add_component(self, component, entity_id):
        component_type = type(component)
        if component_type not in self.component_entities:
            self.component_entities[component_type] = dict()
        if entity_id in self.component_entities[component_type]:
            raise ValueError(f"Entity {entity_id} already has component {component_type.__name__}")
        self.component_entities[component_type][entity_id] = component

    def query(self, *components_types) -> list | list[list] | None:
        if not components_types:
            return None

        for components_type in components_types:
            if components_type not in self.component_entities:
                return None

        keys = self.component_entities[components_types[0]].keys()
        for component in components_types[1:]:
            keys &= self.component_entities[component].keys()

        query = []
        if len(components_types) > 1:
            for key in keys:
                selected_components = []
                for component in components_types:
                    selected_components.append(self.component_entities[component][key])
                query.append(selected_components)
        else:
            for key in keys:
                query.append(self.component_entities[components_types[0]][key])
        return query

    def delete_entity(self, item):
        entity_id = None
        if type(item) in self.component_entities:
            entity_id = item.entity_id
        elif item in self.entity_components:
            entity_id = item
        else:
            raise ValueError(f"No entity id or component was found matching '{item}'.")
        components = self.entity_components[entity_id]
        self.entity_components.pop(entity_id)
        for component in components:
            self.component_entities[type(component)].pop(entity_id)

