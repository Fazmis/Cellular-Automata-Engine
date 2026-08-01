from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


LIFE_WITHOUT_DEATH = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={3},
        survive={0, 1, 2, 3, 4, 5, 6, 7, 8}
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="Life Without Death",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
