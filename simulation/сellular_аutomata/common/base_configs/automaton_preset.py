from dataclasses import dataclass
from .binary_automaton_config import BinaryAutomatonConfig
from .display_automaton_config import DisplayAutomatonConfig


@dataclass
class AutomatonPreset:
    binary_automata_config: BinaryAutomatonConfig
    display_automata_config: DisplayAutomatonConfig
