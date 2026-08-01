from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


MAZE = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={3},
        survive={1, 2, 3, 4, 5}
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="Maze",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
