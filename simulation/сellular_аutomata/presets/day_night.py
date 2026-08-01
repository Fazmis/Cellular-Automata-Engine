from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


DAY_NIGHT = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={3, 6, 7, 8},
        survive={3, 4, 6, 7, 8}
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="Day&Night",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
