from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


CAVES = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={6, 7, 8},
        survive={3, 4, 5, 6, 7, 8}
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="Caves",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
