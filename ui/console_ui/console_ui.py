import curses
from .renderer import Renderer
from .input_mapper import InputMapper


class ConsoleUI:
    def __init__(self):
        self.stdscr = None
        self.renderer = None
        self.input_mapper = None

    def start(self):
        self.stdscr = curses.initscr()
        self.input_mapper = InputMapper(self.stdscr)
        commands_info = self.input_mapper.get_commands_info()
        self.renderer = Renderer(self.stdscr, commands_info=commands_info)

        curses.noecho()  # не отображать вводимые символы
        curses.cbreak()  # сразу получать нажатия
        self.stdscr.keypad(True)  # специальные клавиши
        # не блокировать getch()
        self.stdscr.nodelay(True)

        self.renderer.initialize()

    def stop(self):
        if self.stdscr is None:
            return
        self.stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def render(self, render_data):
        self.renderer.render(render_data)

    def get_commands(self):
        return self.input_mapper.get_commands()