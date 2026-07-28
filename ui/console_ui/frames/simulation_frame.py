import curses
from .windows import HeaderWindow, GameWindow, HelpWindow


class SimulationFrame:
    def __init__(self, stdscr: curses.window, simulation_name:str, grid_size:tuple[int, int], commands):
        self.stdscr = stdscr
        self.title = simulation_name
        self.grid_size = grid_size
        self.commands = commands
        header_lines_count = 3
        self.header_window = HeaderWindow(
            curses.newwin(header_lines_count,
                   20 if len(self.title) < 18 else len(self.title) + 2,
                   0,
                   0),
            self.title,
        )
        self.game_window = GameWindow(
            curses.newwin(
                grid_size[1] + 1,
                grid_size[0] * 2 + 1,
                header_lines_count,
                0,
            ),
            grid_size
        )
        self.help_window = HelpWindow(
            curses.newwin(
                len(commands),
                max(map(len, commands)),
                header_lines_count + grid_size[1] + 1,
                0
            ),
            commands,
        )

    def render(self, render_data=None):
        self.header_window.render()
        self.game_window.render(render_data)
        self.help_window.render()