from dataclasses import dataclass
from .base_component import BaseComponent


@dataclass(slots=True)
class Position(BaseComponent):
    x: int = 0
    y: int = 0
