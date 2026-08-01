import curses


class GameWindow:
    def __init__(self, window: curses._CursesWindow, grid_size: tuple[int, int], cursor):
        self.window = window
        self.grid_size = grid_size
        self.cursor = cursor

    def render(self, grid, config) -> None:
        for position, state in grid:
            x, y = position
            cursor_x, cursor_y = self.cursor.x % self.grid_size[0], self.cursor.y % self.grid_size[1]
            attr = 0
            if cursor_x == x and cursor_y == y:
                attr = curses.A_REVERSE
            self.window.addstr(y, x * 2, config.symbols[state] * 2, attr)

        self.window.noutrefresh()
