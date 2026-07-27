from ui import ConsoleUI
from ecs import Ecs
from simulation import Simulation
from simulation.сellular_аutomata.conway import factory
from engine import Engine


def main():
    gui = ConsoleUI()
    ecs = Ecs()
    simulation = Simulation(ecs)
    simulation.initialize(factory)
    engine = Engine(simulation, gui)
    engine.run()

if __name__ == '__main__':
    main()