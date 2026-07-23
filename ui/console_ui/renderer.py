class Renderer:
    def __init__(self, stdscr, commands_info=""):
        self.stdscr = stdscr
        self.commands_info = commands_info

    def initialize(self):
        self.stdscr.addstr('Игра Дж. Конвея "Жизнь"\n')
        for command in self.commands_info:
            self.stdscr.addstr(f"{command[0]} - {command[1]}")
        self.stdscr.refresh()

    def render(self, render_data):
        self.stdscr.refresh()