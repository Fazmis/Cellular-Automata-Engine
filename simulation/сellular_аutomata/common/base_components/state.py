from dataclasses import dataclass, field
from .base_component import BaseComponent


@dataclass(slots=True)
class State(BaseComponent):
    max_value: int
    value: int = 0
