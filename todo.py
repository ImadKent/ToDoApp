import FreeSimpleGUI as sg
import Todo.functions as functions
sg.theme("lightblue2")
# Creer un label
label = sg.Text("Anime à voir")

# entry input
entry = sg.Input(key="entry_button")
# Creer les boutons
add_button = sg.Button(button_text="Add", key="add_button")
edit_button = sg.Button(button_text="Edit", key="edit_button")
complete_button = sg.Button(button_text="Complete", key="complete_button")

# Creer la list box
list_box = sg.Listbox(values=functions.get_todos('todos.txt'),enable_events=True,key="todo_list", size=(45,10))

# Creer la window
window = sg.Window("My Anime List", layout=[[label],[entry,add_button],[list_box,edit_button],[complete_button]])

while True:
    event,value = window.read()
    print(event)
    print(value)
    if event == sg.WINDOW_CLOSED:
        break

    match event:
        case "add_button":
                selected_todos = value["entry_button"]
                if selected_todos: # verifie si l'entrée n'est pas vide
                    todos = functions.get_todos("todos.txt")
                    todos.append(selected_todos + "\n")
                    functions.write_todos("todos.txt",todos)
                    window["todo_list"].update(todos)
                    window["entry_button"].update("")
                if not selected_todos:
                    sg.popup("Veuillez entrer un anime avant d'ajouter.")
        case "edit_button":
            try:
                selected_todos = value["todo_list"][0]
                todos = functions.get_todos("todos.txt")
                index = todos.index(selected_todos)
                todos[index] = value["entry_button"]
                functions.write_todos("todos.txt",todos)
                window["todo_list"].update(todos)
                window["entry_button"].update("")
            except IndexError:
                sg.popup("Veuillez sélectionner un anime dans la liste avant d'éditer.")

        case "complete_button":
            try:
                selected_todos = value["todo_list"][0]
                todos = functions.get_todos("todos.txt")
                index = todos.index(selected_todos)
                todos.pop(index)
                functions.write_todos("todos.txt",todos)
                window["todo_list"].update(todos)
            except IndexError:
                sg.popup("Veuillez sélectionner un anime à marquer comme complété.")

print(type(functions.get_todos("todos.txt")), functions.get_todos("todos.txt"))
window.close()
