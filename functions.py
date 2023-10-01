FILEPATH = r'C:\Users\hp449\Documents\web_app_1\todo.txt'


def get_todos(filepath=FILEPATH):
    """
    Read a text file and
    Return a list of to-do
    """
    with open(filepath, 'r') as file:
        get_todos_list = file.readlines()
    return get_todos_list


def write_todos(write_todos_list, filepath=FILEPATH):
    """Write the to-do in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(write_todos_list)
