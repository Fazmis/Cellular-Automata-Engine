import curses
from .frames import MainMenuFrame, SimulationFrame
from .input_mapper import InputMapper


class ConsoleUI:
    def __init__(self, size=(20, 20)):
        self.stdscr = None
        self.input_mapper = None
        self.size = size
        self.main_menu_frame = MainMenuFrame
        self.simulation_frame = SimulationFrame
        self.current_frame = None

    def initialize(self) -> None:
        self.stdscr = curses.initscr()

        curses.noecho()  # не отображать вводимые символы
        curses.cbreak()  # сразу получать нажатия
        self.stdscr.keypad(True)  # специальные клавиши
        # не блокировать getch()
        self.stdscr.nodelay(True)

        self.input_mapper = InputMapper(self.stdscr)
        commands_info = self.input_mapper.get_commands_info()
        self.simulation_frame = self.simulation_frame(
            self.stdscr,
            "Conway",
            (20, 20),
            self.input_mapper.get_commands_info()
        )
        self.current_frame = self.simulation_frame

    def shutdown(self) -> None:
        if self.stdscr is None:
            return
        self.stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def render(self, render_data):
        self.current_frame.render(render_data)
        curses.doupdate()

    def get_commands(self):
        return self.input_mapper.get_commands()