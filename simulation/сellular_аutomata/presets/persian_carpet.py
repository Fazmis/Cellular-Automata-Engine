from ..common.base_configs import AutomatonPreset, BinaryAutomatonConfig, DisplayAutomatonConfig


PERSIAN_CARPET = AutomatonPreset(
    binary_automata_config=BinaryAutomatonConfig(
        birth={2, 3, 4},
        survive=set()
    ),
    display_automata_config=DisplayAutomatonConfig(
        title="Persian Carpet",
        symbols={
            0: " ",
            1: "█",
        }
    )
)
