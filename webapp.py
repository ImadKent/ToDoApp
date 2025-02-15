import streamlit as st
import functions

todos = functions.get_todos("../Todo/todos.txt")

def add_todo():
    todo =  st.session_state['new_todo']
    todos = functions.get_todos("../Todo/todos.txt")
    todos.append(todo + "\n")
    functions.write_todos("../Todo/todos.txt",todos)
    st.session_state['new_todo'] = ""


st.title("My Todo App")
st.subheader("this is my Todo app: ")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos("../Todo/todos.txt",todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo",
              placeholder="Enter a new todo",
              on_change=add_todo, key="new_todo")
