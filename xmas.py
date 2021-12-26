"""
xmas.py

A simple christmas tree generator for the terminal.
"""
import os
import random
import time

FILL = "_"  # what will be used next to the tree
SPEED = 0.4  # the seconds between each frame


class Colors:
    NORMAL = '\033[0m'
    GREY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'

    _COLORS = [NORMAL, GREY, RED, GREEN, BLUE, CYAN, WHITE, YELLOW, MAGENTA]


class Light:
    """
    A light in the christmas tree.
    """

    def __init__(self, color):
        """
        Create a light with a color.
        """
        self.color = color

    def __str__(self):
        """
        Return a string representation of the light.
        """
        return "{color}o{normal}".format(color=self.color, normal=Colors.NORMAL)


LIGHTS = [
    Light(Colors.YELLOW),
    Light(Colors.CYAN),
    Light(Colors.MAGENTA)
]

GREEN_LEAF = "{color}*{normal}".format(color=Colors.GREEN, normal=Colors.NORMAL)
underscores = FILL * 14
TRUNK = '\n'.join([underscores + "{color}mWm{normal}".format(color=Colors.YELLOW, normal=Colors.NORMAL) + underscores for _ in range(3)])
CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"

try:
    while True:  # exit with ctrl+C
        print('Exit by pressing down Ctrl+C')
        for i in range(1, 30, 2):  # tree
            tree = ''.join([str(random.choice(LIGHTS)) if random.random() >= 0.5 else GREEN_LEAF for _ in range(i)])
            underscores = FILL * (15 - i // 2)
            print(underscores + tree + underscores)
        print(TRUNK)
        message = "{color}Merry Christmas{normal}".format(color=random.choice(Colors._COLORS), normal=Colors.NORMAL)
        underscores = FILL * 8
        print(underscores + message + underscores)
        time.sleep(SPEED)
        os.system(CLEAR_COMMAND)
except Exception:
    from traceback import print_exc
    print_exc()
    print(Colors.NORMAL)
    print("Good bye and Merry Christmas 🎄!")
