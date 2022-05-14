import re

def sanitize_input(str):
    legal_input = "[^A-Za-z0-9]+"
    return re.sub(legal_input, '', str)
        
def sanitize_input_numbers(str):
    legal_input = "[^0-9]+"
    return re.sub(legal_input, '', str)

def sanitize_input_date(str):
    legal_input = "[^0-9-]+"
    return re.sub(legal_input, '', str)

def sanitize_input_letters(str):
    legal_input = "[^A-Za-z]+"
    return re.sub(legal_input, '', str)