from ui import ConsoleUI
from simulation import Simulation
from engine import Engine


def main():
    gui = ConsoleUI()
    simulation = Simulation()
    engine = Engine(simulation, gui)
    engine.run()

if __name__ == '__main__':
    main()