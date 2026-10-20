def format_name(first, last, uppercase=False):
    if uppercase==True:
        return first.upper() + " " + last.upper()
    return first + " " + last