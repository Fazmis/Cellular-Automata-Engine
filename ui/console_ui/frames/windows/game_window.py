import curses


class GameWindow:
    def __init__(self, window: curses.window, grid_size: tuple[int, int]):
        self.window = window
        self.grid_size = grid_size

    def render(self, render_data):
        if render_data is not None:
            for position, alive in render_data:
                x, y = position
                self.window.addstr(y, x + x, "██" if alive else "  ")
        self.window.noutrefresh()
