FILEPATH = "todos.txt"
# this is a local module
# import function to call it
# should be on the same directory as main
# you can also say from function import get_tods, write_todos
# if you put this local module in other file you need to do from module import functions

def get_todos(filepath=FILEPATH):
    """ read a text file and return the list of
        to do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local  # here we do return as we need the list value of todos = []


def write_todos(todos_arg, filepath=FILEPATH):  # non default parameter todos_arg should always be before default
    """ Write the to do list items in a text file
    """
    with open(filepath, "w") as file_local:  # here todos_arg is the arg we want to write
        file_local.writelines(todos_arg)  # here we don't need return as we are only writing


if __name__ == "__main__":  # this won't allow print to run "hello" when we use cli.py.
    print("hello")  # this will only run when we use functions.py
    print(get_todos())  # the __name__ changes to function when we call it on cli.py
    # if condition becomes false
