# from functions import get_todos, write_todos
import functions
# if you only import functions you need to do functions.get_todos()
import time

now = time.strftime("%b %d, %Y %H %M %S")
print("It is", now)

text = """
this is a a multi line string.
This is a todo app
type add "your to do list" to add a list 
type edit "a number" to select the list you want to edit
something like that
"""

print(text)

while True:
    user_input = input("Enter add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        user_action = user_input[4:]
        if user_action.isdigit():
            print("Enter a list todo")
            continue

        else:
            print(f"{user_action} has been added to list")

        todos = functions.get_todos()

        todos.append(user_action + "\n")

        functions.write_todos(todos)

    elif user_input.startswith("show"):

        todos = functions.get_todos("todos.txt")

        strip_todo = [item.strip("\n") for item in todos]

        for index, items in enumerate(strip_todo):
            print(f"{index + 1}-{items}")

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = functions.get_todos()

            if number not in range(len(todos)):
                print("List not found")
                continue

            new_todo = input("Enter a new todo list: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Enter a number after edit")

        except IndexError:
            print(f"The number not found in list")

    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])

            todos = functions.get_todos()

            number = number - 1

            todos.pop(number)

            functions.write_todos(todos)

        except ValueError:
            print("Place a number after complete")
        except IndexError:
            print(f"The List does not have that number")
        else:
            print(f"List {number + 1} has been completed")

    elif user_input.startswith("exit"):
        break
    else:
        print("Command invalid")

print("Exited")
