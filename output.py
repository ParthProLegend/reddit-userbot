COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'bright_purple': '\033[95m',
    'cyan': '\033[96m',
    'bright_gray': '\033[90m',
    'white': '\033[37m',
    'purple': '\033[35m',
    'black': '\033[30m',
    'reset': '\033[0m'
}

def print_color(text, color, end=""):
    print(f"{COLORS.get(color, COLORS['reset'])}{text}{COLORS['reset']}", end=end)

def prRed(s, end=""): print_color(s, 'red', end)
def prGreen(s, end=""): print_color(s, 'green', end)
def prYellow(s, end=""): print_color(s, 'yellow', end)
def prBlue(s, end=""): print_color(s, 'blue', end)
def prBrightPurple(s, end=""): print_color(s, 'bright_purple', end)
def prPurple(s, end=""): print_color(s, 'purple', end)
def prCyan(s, end=""): print_color(s, 'cyan', end)
def prBrightGray(s, end=""): print_color(s, 'bright_gray', end)
def prBlack(s, end=""): print_color(s, 'black', end)

class ColorCycler:
    def __init__(self):
        self.n = 0

    def cycling_colors_print(self, line):
        self.line = line
        COLORS_LIST = [key for key in COLORS.keys() if key not in ['reset', 'black', 'purple']]
        for character in self.line:
            if character.isprintable() and character not in ' \n\t':
                prColor = COLORS_LIST[self.n % len(COLORS_LIST)]
                print_color(character, prColor, end='')
                self.n += 1
            else:
                print(character, end='')


if __name__ == "__main__":
    line = "This is not the main file, just to get colored output in terminal like this. 1234567890\n"
    Colour = ColorCycler()
    Colour.cycling_colors_print(line)
    prPurple("Run main.py now!")