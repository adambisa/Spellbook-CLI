import pyfiglet
from rich import print


def help_dnd():
    title = pyfiglet.figlet_format('Hello', font='isometric2')
    print(f'[yellow]{title}[/yellow]')


def initialize():
    print("")
