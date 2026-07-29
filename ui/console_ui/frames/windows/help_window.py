import curses

class HelpWindow:
    def __init__(self, window: curses._CursesWindow):
        self.window = window
        self.help = [
            "q - exit",
            "←→↑↓ - move cursor",
            "space - edit cell",
            "enter - next step",
            "backspace - previous step"
        ]
        for i, row in enumerate(self.help):
            self.window.addstr(i + 1, 0, row)

    def render(self, generation):
        self.window.clrtoeol()
        generation_str = "Generation: " + str(generation)
        self.window.addstr(0, 0, generation_str)
        self.window.noutrefresh()
