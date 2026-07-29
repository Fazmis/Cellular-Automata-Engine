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
            self.window.addstr(i + 2, 0, row)

    def render(self, generation_step, state):
        self.window.move(0, 0)
        self.window.clrtoeol()
        self.window.move(1, 0)
        self.window.clrtoeol()
        generation_str = "Generation: " + str(generation_step)
        state_str = "State: " + str(state)
        self.window.addstr(0, 0, generation_str)
        self.window.addstr(1, 0, state_str)
        self.window.noutrefresh()

