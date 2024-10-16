def generate_message(name):
    if not name:
        raise ValueError("Name is missing")
    '''Generate a morning greeting message'''
    return f"Good Morning, {name}! Have a wonderful day!"

