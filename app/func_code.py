import os
import datetime

def create_dir():
    dir_name = 'notes'
    its_folder = os.path.isdir(dir_name)
    if its_folder == True:
        return its_folder
    else:
        os.mkdir(dir_name)
        print(f'Папка {dir_name} успешно создана\n')        

def create_note():
    title = input("Введите заголовок заметки: ")
    filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%S')}_{title}"
    filepath = os.path.join("notes", filename)
    text = input("Введите содержимое заметки: ")
    with open(filepath, "w") as file:
        file.write(text)
    print(f"Заметка {title} успешно создана")

def view_notes():
    notes = os.listdir("notes")
    if not notes:
        print("Заметки отсутствуют")
    else:
        for note in notes:
            with open(os.path.join("notes", note), "r") as file:
                print(f"\n{note}")
                print(file.read())


def edit_notes():
    notes = os.listdir("notes")
    if not notes:
        print("Заметки отсутствуют")
    else:
        for i, n in enumerate(notes):
            print(f"{i + 1}. {n}")
        choice = int(input("Выберите номер заметки для редактирования: "))
        filename = os.path.join("notes", notes[choice - 1])
        with open(filename, "r") as file:
            text = file.read()
        print(f"Текущее содержимое заметки: \n{text}")
        new_text = input("Введите новое содержимое заметки: ")
        with open(filename, "w") as file:
            file.write(new_text)
        print("Заметка успешно отредактирована")       

def delete_note():
    notes = os.listdir("notes")
    if not notes:
        print("Заметки отсутствуют")
    else:
        for i, n in enumerate(notes):
            print(f"{i + 1}. {n}")
        choice = int(input("Выберите номер заметки для удаления: "))
        filename = os.path.join("notes", notes[choice-1])
        os.remove(filename)
        print("Заметка успешно удалена") 