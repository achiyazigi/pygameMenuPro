from pygame import display
from pygameMenuPro import *

# Lets finish with the pygame stuff...
pygame.init()
pygame.display.set_caption('title')

WIDTH = 1080
HEIGHT = WIDTH//1.6
WINDOW_SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE, depth=32)

# Define some constants:
TITLE_POS = (screen.get_width()//2, screen.get_height()//4)

OPTIONS_MENU_COLOR = Color(38, 91, 200)

# Set your own default fonts.
# you can always choose something different in a specific instance...
Option.font.set_default_option(pygame.font.SysFont('Comic Sans MS', 50))
Option.font.set_default_title(pygame.font.SysFont('Comic Sans MS', 80))
Option.font.set_default_highlight(pygame.font.SysFont('Comic Sans MS', 50, bold=True))

# Define your listeners.
# It's recommanded to define them on the go
# while you define your options.
def start_game():
    """
    Shows a blue screen representing the game has started
    """
    menu.run_display = False
    while(True):
        screen.fill(Color(0, 0, 255))
        Option.input.check_input()
        Option.clock.tick(60)
        display.update()
        Option.input.reset()


def scroll_to_change(option: Option):
    """
    Enables scrolling to change an active input option
    """
    if(Option.input.mouse_wheel[1] < 0 and option.input_output > 0):
        option.input_output -= 1
    elif(Option.input.mouse_wheel[1] > 0 and option.input_output < 100):
        option.input_output += 1


def quit_menu(menu: Menu):
    """
    Back to previous menu.
    If main menu then the control passes back to main code
    """
    menu.run_display = False
    Option.input.reset()

# start option for starting the game.
# Note that you don't have to add highlight but it's recommanded
start = Option('Start')\
    .add.highlight()\
    .add.select_listener(lambda _: start_game()) # (Subscribing start_game to 'on_select' event)

# Volume option for volume adjustment. (in options menu)
volume = Option('volume')\
    .add.highlight()\
    .add.input(0)\
    .add.active_listener(scroll_to_change)

# Difficulty option for Difficulty adjustment. (in options menu)
difficulty = Option('Difficulty Level:')\
    .add.highlight()\
    .add.input(0)\
    .add.active_listener(scroll_to_change)

# Back to Main Menu
back = Option('Back To Main Menu')\
    .add.highlight()\
    .add.select_listener(lambda _: quit_menu(options))

# An encapsulated menu.
# By default selecting that option will run this menu display.
# set_options will set the input list as this menu's options.
options = Option('Options', color=OPTIONS_MENU_COLOR)\
    .add.mouse_menu(screen, TITLE_POS, background_color=OPTIONS_MENU_COLOR)\
    .set_options([volume, difficulty, back])\
    .add.highlight()\
    .add.select_listener(lambda _: Option.input.reset())

# Lets leave this option blank for you to see the default behavior...
credits = Option('Credits')\
    .add.highlight()

# Exit main menu and return to user's program code:
quit = Option('Quit')\
    .add.highlight()\
    .add.select_listener(lambda _: quit_menu(menu))

# Setting the main menu and its options
menu = Option('menu').add.mouse_menu(screen, TITLE_POS).set_options([
    start,
    options,
    credits,
    quit
])

# Starting menu's loop.
# The loop can be interrupted nicely by menu.run_display = False.
# One example for such interrupt is in quit_menu above...
menu.display_menu()

# game.vol = volume.input_output
# game.level = difficulty.input_output

# while(not game.over):
#     ...
