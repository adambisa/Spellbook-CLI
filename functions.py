import pyfiglet
from rich import print
from random import choice
import json

classes = ["barbarian", "bard", "cleric", "druid",
           "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "wizard", "warlock"]

def help_dnd():
    title = pyfiglet.figlet_format('SpellbookCLI', font="doom")
    print(f'[red]{title}[/red]')
    print(f'Welcome Adventurers, warm around my fire and tell me a tale.')
    print(f'Usage : python3 main.py [-h|help] OR [-f|fill] [-n|name "someName"] OR [-i|init] OR [-u|update] OR [-p|prepare] OR [-c|color]') 
    all_monsters = ["Goblins", "Dragons", "Mindflayers", "Cultists", "Demons", "Devils", "Beasts", "Giants", "Gods"]
    monsters = choice(all_monsters)
    print(f'Hope this was enough of an explanation, now get ready to slay some [red]{monsters}[/red] !')

def initialize():
    name = input("Choose a name for your hero: ")
    class_dnd = input("Which class are you playing? ")
    if class_dnd.lower() not in classes:
        print("[red]Invalid class supplied. Roll for initiative. [/red]")
    lvl_dnd = input("Which lvl are you? ")
    bonus = input("What is your bonus to your spellcasting modifier? ")
    try:
        int(lvl_dnd)
    except ValueError:
        print("[red]Invalid level supplied. Roll for initiative. [/red]")
        return
    finally:
        lvl_dnd = int(lvl_dnd)
    try:
        int(bonus)
    except ValueError:
        print("[red]Invalid ability modifier supplied. Roll for initiative. [/red]")
        return
    finally:
        bonus = int(bonus)
    if lvl_dnd > 20:
        print("[red]Level supplied is too high, perhaps you had too much homebrew. [/red]")
        return
        
        
    num_of_prepared_spells = lvl_dnd + bonus

    data = {'name': name, 'class': class_dnd, 'lvl':lvl_dnd, 'modifier':bonus, 'total_spells': num_of_prepared_spells, 'spells' : [], 'cantrips':[]}
    with open(f'{name}.json', 'w') as f:
        json.dump(data, f) 
    print(f"[green]The spellbook for hero {name} has been initialized. Save travels, wanderer.[/green]")
    print(f"[green]Feel free to proceed and fill your spellbook, so you can prepare spells later.[/green]")


def fill_spellbook(name:str):
    """
    open shit by name check lvl, provide options for spells from json i get from api really easy
    """
    with open(f"{name}.json", "r") as f:
        print(f"{f.read()}")