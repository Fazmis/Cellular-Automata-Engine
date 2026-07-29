from dataclasses import dataclass

@dataclass()
class AutomataConfig:
    states_count: int
    symbols: dict[int, str]
