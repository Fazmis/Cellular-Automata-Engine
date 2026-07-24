from dataclasses import dataclass
from base_component import BaseComponent


@dataclass(slots=True)
class IsAlive(BaseComponent):
    alive: bool = False
