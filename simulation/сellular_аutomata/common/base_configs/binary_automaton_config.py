from dataclasses import dataclass


@dataclass
class BinaryAutomatonConfig:
    birth: set[int]
    survive: set[int]
