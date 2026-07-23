from .commands import Command

class Engine:
    def __init__(self, simulation, gui):
        self.simulation = simulation
        self.gui = gui
        self.running = False

    def _loop(self):
        while self.running:
            # user input
            commands = self.gui.get_commands()

            # commands processing
            for command in commands:
                self.execute(command)

            render_data = self.simulation.get_render_data()

            # render
            self.gui.render(render_data)

    def run(self):
        self.running = True
        self.gui.start()
        try:
            self._loop()
        finally:
            self.gui.stop()

    def stop(self):
        self.running = False

    def execute(self, command:Command):
        match command:
            case Command.EXIT:
                self.stop()
