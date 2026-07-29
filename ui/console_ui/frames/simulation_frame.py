import curses
from .windows import HeaderWindow, GameWindow, HelpWindow


class SimulationFrame:
    def __init__(self, stdscr: curses._CursesWindow, cursor, simulation_name:str, grid_size:tuple[int, int]):
        self.stdscr = stdscr
        self.cursor = cursor
        self.title = simulation_name
        self.grid_size = grid_size
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
                header_lines_count + 1,
                0,
            ),
            grid_size,
            self.cursor
        )
        self.help_window = HelpWindow(
            curses.newwin(
                7,
                50,
                header_lines_count + grid_size[1] + 1,
                0
            ),
        )

    def render(self, render_data:dict):
        self.header_window.render(render_data.get("title"))

        grid = render_data.get("grid")
        config = render_data.get("grid_config")
        self.game_window.render(grid, config)

        generation_step = render_data.get("generation_step")
        state = render_data.get("state")
        self.help_window.render(generation_step, state)
