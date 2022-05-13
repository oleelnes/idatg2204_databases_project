import re

def sanetize_input(str):
    legal_input = "[^A-Za-z0-9]+"
    return re.sub(legal_input, '', str)
        