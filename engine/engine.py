from .clock import Clock
from .commands import Command

class Engine:
    def __init__(self, simulation, gui):
        self.simulation = simulation
        self.gui = gui
        self.clock = Clock()
        self.running = False

    def _loop(self):
        while self.running:
            # user input
            commands = self.gui.get_commands()

            # commands processing
            for command, payload in commands:
                self.execute(command, payload)

            render_data = self.simulation.get_render_data()

            # render
            self.gui.render(render_data)

            self.clock.tick()

    def run(self):
        self.running = True
        self.gui.initialize()
        try:
            self.clock.reset()
            self._loop()
        finally:
            self.gui.shutdown()

    def stop(self):
        self.running = False

    def execute(self, command:Command, payload):
        match command:
            case Command.EXIT:
                self.stop()
            case Command.EDIT_CELL:
                self.simulation.change_cell(payload)
            case Command.NEXT_STEP:
                self.simulation.next_step()
