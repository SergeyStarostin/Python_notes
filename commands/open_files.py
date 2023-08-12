import os

from view import texts
from models.notes import Notes


def open_notes():
    """Функция для открытия выбранной базы заметок в формате CSV"""
    print(texts.file_name)
    file_name = input()
    csv_file = f"{file_name}.csv"
    notes = Notes.get_instance()
    notes_list = []

    if os.path.exists(csv_file):
        notes_list = notes.load_from_file(csv_file)
    else:
        print(texts.file_not_found, {file_name})
    notes.notes.extend(notes_list)
    print(texts.file_added_successfully, {file_name})
