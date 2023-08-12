import os

from view import texts
from view.view import view_notes
from models.notes import Notes
from commands.create_note import CreateNoteCommand
from commands.edit_note import EditNoteCommand
from commands.delete_note import DeleteNoteCommand
from commands.open_list_files import list_files
from commands.open_files import open_notes


def print_menu():
    """Функция выводит на экран главное меню."""
    print(*texts.menu, sep='')


def controller():
    """Функция управления приложением с заметками."""
    notes = Notes.get_instance()

    while True:
        print_menu()
        choice = input(texts.choice)

        if choice == '1':
            """Пункт меню "Создать заметку"."""
            print(texts.input_id)
            id = input()
            print(texts.input_title)
            title = input()
            print(texts.input_text)
            text = input()
            c = CreateNoteCommand(notes, id, title, text)
            c.execute()

        elif choice == '2':
            """Пункт меню "Удалить заметку"."""
            print(texts.input_id)
            id = input()
            print(texts.confirm_delete)
            while True:
                if input() == 'y':
                    d = DeleteNoteCommand(notes, id)
                    d.execute()
                    break
                elif input() == 'n':
                    print(texts.deletion_canceled)
                    break
                else:
                    print(texts.incorrect_input)
                    break

        elif choice == '3':
            """Пункт меню "Редактировать заметку"."""
            print(texts.input_id)
            id = input()
            print(texts.new_values)
            print(texts.input_title)
            title = input()
            print(texts.input_text)
            text = input()
            e = EditNoteCommand(notes, id, title, text)
            e.execute()

        elif choice == '4':
            """Пункт меню "Показать все заметки"."""
            view_notes(notes)

        elif choice == '5':
            """Пункт меню "Сохранить заметки в файл"."""
            print(texts.save_to_file)
            file_ext = input(texts.file_ext)
            os.environ['file_ext'] = file_ext
            notes.save_to_file()
            print(texts.successfully_saved)

        elif choice == '6':
            """Пункт меню "Отобразить список файлов"."""
            list_files()

        elif choice == '7':
            """Пункт меню "Открыть базу заметок из файла"."""
            open_notes()

        elif choice == '8':
            """Выход из программы."""
            break

        else:
            """Вывод сообщения об ошибке, при некорректном вводе."""
            print(texts.incorrect_input)
