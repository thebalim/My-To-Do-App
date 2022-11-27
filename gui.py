import functions
import PySimpleGUI as sg
import time

sg.theme("LightBlue7")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", size=13)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=(45, 10), enable_events=True)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H %M %S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                edit_to_do = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(edit_to_do)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a list first", font=("Helvetica", 10))
            else:
                continue
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                complete_todo = values["todos"][0]
                todos = functions.get_todos()
                index = todos.index(complete_todo)
                todos.pop(index)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a list", font=("Helvetica", 15))
            else:
                continue
        case sg.WIN_CLOSED | "Exit":
            break

window.close()
