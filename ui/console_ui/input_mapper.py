import curses
from .frames import MainMenuFrame, SimulationFrame
from engine import Command


class InputMapper:
    def __init__(self, stdscr, current_frame) -> None:
        self.stdscr = stdscr
        self.current_frame = current_frame
        self.keymaps = {
            SimulationFrame: {
                ord("q"): Command.EXIT,
                ord(" "): Command.EDIT_CELL,
                ord("\n"): Command.NEXT_STEP,
                ord("\x08"): Command.PREVIOUS_STEP,
            },
            MainMenuFrame: {
                ord("q"): Command.EXIT,
                ord("\n"): Command.SELECT_SIMULATION,
            },
            "cursor": {
                curses.KEY_RIGHT: (1, 0),
                curses.KEY_LEFT: (-1, 0),
                curses.KEY_DOWN: (0, 1),
                curses.KEY_UP: (0, -1),
            }
        }

    def get_commands(self) -> list[dict[Command, list]]:
        commands = []
        while True:
            key = self.stdscr.getch()
            if key == -1:
                break
            if curses.KEY_DOWN <= key <= curses.KEY_RIGHT:
                self.current_frame.cursor += self.keymaps["cursor"][key]
                continue

            command = self.keymaps[type(self.current_frame)].get(key)
            if command is None:
                continue

            payload = None
            match command:
                case Command.EDIT_CELL:
                    cursor = self.current_frame.cursor
                    payload = (cursor.x, cursor.y)
                case Command.SELECT_SIMULATION:
                    selected_simulation = self.current_frame.get_selected_simulation()
                    payload = selected_simulation
            commands.append((command, payload))

        return commands

    def get_commands_info(self) -> list[tuple[str, str]]:
        commands_info = [
            (chr(key), value.name) for key, value in self.keymaps[type(self.current_frame)].items()
        ]
        return commands_info
