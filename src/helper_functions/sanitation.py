import re

def sanitize_input(str_in):
    if isinstance(str_in, str):
        legal_input = "[^A-Za-z0-9]+"
        return re.sub(legal_input, '', str_in)
    else:
        return str_in
        
def sanitize_input_numbers(str_in):
    if isinstance(str_in, str):
        legal_input = "[^0-9]+"
        return re.sub(legal_input, '', str_in)
    else:
        return str_in

def sanitize_input_date(str_in):
    if isinstance(str_in, str):
        legal_input = "[^0-9-]+"
        return re.sub(legal_input, '', str_in)
    else:
        return str_in

def sanitize_input_letters(str_in):
    if isinstance(str_in, str):
        legal_input = "[^A-Za-z]+"
        return re.sub(legal_input, '', str_in)
    else:
        return str_in