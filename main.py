# from functions import get_todos, write_todos ---- altro modo per importare funzioni da un file
import functions  # se ci fosse cartella diversa: from nome_cartella import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print("It is ", now)
while True:
    user_action = input("Type add, show, edit, delete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            number = int(user_action[5:])
            todos[number - 1] = input("New todo: ") + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Not valid number after edit")
            continue

    elif user_action.startswith("delete"):
        try:
            todos = functions.get_todos()

            number = int(user_action[7:])
            removed_todo = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)

            print(f"Todo {removed_todo} was removed from the list!")
        except IndexError:
            print("Invalid number of item")
            continue
    elif 'exit' in user_action:
        break
    else:
        print("Invalid command")

print('Bye!')
