import os
import ctypes


def prepare_console(width: int = 60, height: int = 40):
    """
    Увеличивает размер окна и очищает буфер консоли Windows.
    """

    if os.name != "nt":
        return

    kernel32 = ctypes.windll.kernel32

    class COORD(ctypes.Structure):
        _fields_ = [
            ("X", ctypes.c_short),
            ("Y", ctypes.c_short),
        ]

    class SMALL_RECT(ctypes.Structure):
        _fields_ = [
            ("Left", ctypes.c_short),
            ("Top", ctypes.c_short),
            ("Right", ctypes.c_short),
            ("Bottom", ctypes.c_short),
        ]

    STD_OUTPUT_HANDLE = -11

    handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    if not handle:
        return

    # Сначала увеличиваем буфер с запасом
    buffer_size = COORD(width, height)
    kernel32.SetConsoleScreenBufferSize(handle, buffer_size)

    # Потом задаём окно
    window = SMALL_RECT(
        0,
        0,
        width - 1,
        height - 1
    )

    kernel32.SetConsoleWindowInfo(
        handle,
        True,
        ctypes.byref(window)
    )
    os.system("cls")