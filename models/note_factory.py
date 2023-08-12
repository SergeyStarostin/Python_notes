from models.note import Note
from datetime import datetime


class NoteFactory:
    """Фабрика для создания экземпляров заметок"""

    @staticmethod
    def create(id, title, text):
        """Метод статического класса, который создает новый экземпляр класса Note с указанными параметрами.
        id - идентификатор заметки,
        title - заголовок заметки,
        text - текст заметки,
        created - текущая дата и время создания заметки,
        modified - текущая дата и время изменения заметки.
        """
        return Note(id, title, text, datetime.now(), datetime.now())
