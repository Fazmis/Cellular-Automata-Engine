from dataclasses import dataclass


@dataclass()
class DisplayAutomatonConfig:
    title: str
    symbols: dict[int, str]

    @property
    def states_count(self) -> int:
        return len(self.symbols)
