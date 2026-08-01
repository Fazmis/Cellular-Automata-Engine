from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


HIGH_LIFE = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={3, 6},
        survive={2, 3}
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="High Life",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
