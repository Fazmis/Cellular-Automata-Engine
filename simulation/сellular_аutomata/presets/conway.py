from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


CONWAY = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={3},
        survive={2, 3}
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="Conway Game Of Life",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
