import curses

class HelpWindow:
    def __init__(self, window: curses.window, commands):
        self.window = window
        self.commands = commands

    def render(self):
        self.window.noutrefresh()