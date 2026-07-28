import curses

class HeaderWindow:
    def __init__(self, window: curses.window, title:str):
        self.window = window
        self.title = title
        self.window.addstr(title)

    def render(self):
        self.window.noutrefresh()