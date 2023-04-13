import excepts as exc
import func_code as fc

def user_menu():
    fc.create_dir()
    action = ["\n1 - Просмотр заметок", "2 - Создание заметки",
              "3 - Редактирование заметки", "4 - Удаление заметки", "5 - Выход\n"]

    for i in action:
        print(i)     

def user_choice(num):
    if num == 1:
        print()
        fc.view_notes()
        return user_choice(exc.check_number())
    elif num == 2:
        print()
        fc.create_note()
        return user_choice(exc.check_number())
    elif num == 3:
        print()
        fc.edit_notes()
        return user_choice(exc.check_number())
    elif num == 4:
        print()
        fc.delete_note()
        return user_choice(exc.check_number())
    elif num == 5:
        print()
        return exit()
    else:
        print()
        return user_choice(exc.check_number())      