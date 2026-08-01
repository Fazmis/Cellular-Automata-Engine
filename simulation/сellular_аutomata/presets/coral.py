from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


CORAL = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={3},
        survive={4, 5, 6, 7, 8}
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="Coral",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
