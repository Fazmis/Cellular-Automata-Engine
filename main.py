from ui import ConsoleUI
from ecs import Ecs
from simulation import Simulation
from simulation.сellular_аutomata.presets import CONWAY
from engine import Engine


def main() -> None:
    gui = ConsoleUI()
    ecs = Ecs()
    simulation = Simulation(ecs)
    simulation.initialize(CONWAY)
    engine = Engine(simulation, gui)
    engine.run()


if __name__ == '__main__':
    main()
