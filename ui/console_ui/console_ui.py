import curses

from .cursor import Cursor
from .input_mapper import InputMapper
from .frames import MainMenuFrame, SimulationFrame


class ConsoleUI:
    def __init__(self, size=(20, 20)):
        self.size = size
        self.stdscr = None
        self.cursor = Cursor()
        self.input_mapper = None
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

        self.input_mapper = InputMapper(self.stdscr, self.cursor)
        self.simulation_frame = self.simulation_frame(
            self.stdscr,
            self.cursor,
            "Conway",
            (20, 20),
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