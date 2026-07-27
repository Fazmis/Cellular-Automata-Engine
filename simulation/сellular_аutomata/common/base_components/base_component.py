from dataclasses import dataclass, field

@dataclass(slots=True)
class BaseComponent:
    entity_id: int | None = field(default=None, init=False, repr=False)
