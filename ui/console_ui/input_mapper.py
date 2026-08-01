import curses
from engine import Command


class InputMapper:
    def __init__(self, stdscr, cursor) -> None:
        self.stdscr = stdscr
        self.cursor = cursor
        self.keymap = {
            ord("q"): Command.EXIT,
            ord(" "): Command.EDIT_CELL,
            ord("\n"): Command.NEXT_STEP,
            ord("\x08"): Command.PREVIOUS_STEP
        }

    def get_commands(self) -> list[dict[Command, list]]:
        commands = []
        while True:
            key = self.stdscr.getch()
            if key == -1:
                break
            if curses.KEY_DOWN <= key <= curses.KEY_RIGHT:
                match key:
                    case curses.KEY_RIGHT:
                        self.cursor.x += 1
                    case curses.KEY_LEFT:
                        self.cursor.x -= 1
                    case curses.KEY_DOWN:
                        self.cursor.y += 1
                    case curses.KEY_UP:
                        self.cursor.y -= 1
                continue

            command = self.keymap.get(key)
            if command is None:
                continue

            payload = None
            match command:
                case Command.EDIT_CELL:
                    payload = (self.cursor.x, self.cursor.y)

            commands.append((command, payload))

        return commands

    def get_commands_info(self) -> list[tuple[str, str]]:
        commands_info = [
            (chr(key), value.name) for key, value in self.keymap.items()
        ]
        return commands_info
