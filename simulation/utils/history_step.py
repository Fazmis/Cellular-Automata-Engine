from dataclasses import dataclass


@dataclass
class Step:
    snapshot: dict
    hash: int
