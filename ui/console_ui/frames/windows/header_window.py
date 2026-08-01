import curses


class HeaderWindow:
    def __init__(self, window: curses._CursesWindow, title: str):
        self.window = window
        self.title = title

    def render(self, config) -> None:
        self.window.addstr(1, 0, config.title)
        self.window.noutrefresh()
