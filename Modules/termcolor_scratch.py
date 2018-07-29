from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan")

# print(help(termcolor))
print(colored("Here's my string", "magenta", "on_green"))


# ==================================

def color_figgy(text, color):
    if color not in valid_colors:
        print("invalid color")
        color = "magenta"

    words = figlet_format(text)
    font_color = colored(words, color)
    return font_color


# When you want to prevent a block of code from running on an import
if __name__ == "__main__":
    print(color_figgy("Ain't this a bitch", "sss"))
    print(color_figgy("Shit works", "cyan"))