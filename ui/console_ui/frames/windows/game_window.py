import curses


class GameWindow:
    def __init__(self, window: curses.window, grid_size: tuple[int, int], cursor):
        self.window = window
        self.grid_size = grid_size
        self.cursor = cursor

    def render(self, render_data):
        if render_data is not None:
            for position, alive in render_data:
                x, y = position
                cursor_x, cursor_y = self.cursor.x % self.grid_size[0], self.cursor.y % self.grid_size[1]
                attr = 0
                if cursor_x == x and cursor_y == y:
                    attr = curses.A_REVERSE
                self.window.addstr(y, x + x, "██" if alive else "  ", attr)
        else:
            for y in range(self.grid_size[1]):
                self.window.addstr(y, 0, "  " * self.grid_size[0])


        self.window.noutrefresh()
