"""
author : adambisa
tool to prepare and manage spells using api below 
might add other functionality but idk rn 
3.3.25
"""

import requests
import sys
# terrible practice to import all but ill just be adding and adding fix this later
from functions import *

base_url = "https://www.dnd5eapi.co/"




args = sys.argv


"""
there needs to be a certain amount of args, ill just add shit here over time


i am thinking something like  py main.py [init|-i] OR [prep|-p] OR [update|-u] OR [help|-h]
"""

if len(args) == 2 :
    match args[1]:
        case "-i":
            initialize()
        case "init":
            initialize()
        case "-h":
            help_dnd()
        case "help":
            help_dnd()
elif len(args) == 3:
    match args[1]:
        case "-n":
            fill_spellbook(args[2])
        case "name":
            fill_spellbook(args[2])
else:
    help_dnd()