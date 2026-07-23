from commands import Command

class InputMapper:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.keymap = {
            ord("q"): Command.EXIT
        }

    def get_commands(self) -> list[Command]:
        commands = []
        while True:
            key = self.stdscr.getch()
            if key == -1:
                break
            command = self.keymap.get(key)
            if command:
                commands.append(command)

        return commands

    def get_commands_info(self) -> list[tuple[str, str]]:
        commands_info = [
            (chr(key), value.name) for key, value in self.keymap.items()
        ]
        return commands_info
