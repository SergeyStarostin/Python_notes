import os
import csv
import chardet

from view import texts
from datetime import datetime
from models.note_factory import NoteFactory
from models.note import Note


class Notes:
    """Класс заметок"""
    _instance = None

    @staticmethod
    def get_instance():
        if not Notes._instance:
            Notes._instance = Notes()
        return Notes._instance

    def __init__(self):
        """Конструктор класса Notes возбуждает исключение в случае повторного создания экземпляра класса."""
        if Notes._instance != None:
            raise Exception(texts.exception_in)
        else:
            Notes._instance = self
            self.notes = []

    def create(self, id, title, text):
        """Метод для создания заметки
        id - идентификатор заметки,
        title - заголовок заметки,
        text - текст заметки.
        """
        note = NoteFactory.create(id, title, text)
        self.notes.append(note)
        print(texts.note_created, note)

    def delete(self, id):
        """Метод для удаления заметки
        id - идентификатор удаляемой заметки.
        """
        note = self.get_note_by_id(id)
        if note:
            self.notes.remove(note)
            print(texts.note_deleted, note)
        else:
            print(texts.note_not_found, id)

    def edit(self, id, title=None, text=None):
        """Метод для редактирования заметки по идентификатору
        id - идентификатор заметки, которую нужно отредактировать,
        title - новый заголовок заметки,
        text - новый текст заметки.
        """
        note = self.get_note_by_id(id)
        if note:
            if title:
                note.title = title
            if text:
                note.text = text
            note.modified = datetime.now()
            print(texts.note_edited, note)
        else:
            print(texts.note_not_found, id)

    def read(self, filter_date=None):
        """Метод для чтения заметок
        filter_date - дата для фильтрации заметок по дате создания или изменения,
        list - список заметок.
        """
        if not self.notes:
            return []
        if filter_date:
            filtered_notes = [note for note in self.notes if
                              note.created.date() == filter_date.date() or note.modified.date() == filter_date.date()]
            if filtered_notes:
                return filtered_notes
            else:
                return []
        return self.notes

    def get_note_by_id(self, id):
        """Метод для получения заметки по идентификатору
        id - идентификатор заметки.
        """
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def save_to_file(self):
        """Метод для сохранения заметок в файл
        unique_ids - множество для хранения уникальных идентификаторов заметок,
        unique_notes - список для хранения заметок с уникальными идентификаторами.
        """
        notes = [note.to_dict() for note in self.notes]
        unique_ids = set()
        unique_notes = []
        for note in notes:
            if note['id'] not in unique_ids:
                unique_ids.add(note['id'])
                unique_notes.append(note)

        file_ext = os.getenv('file_ext', 'csv')
        if file_ext == 'csv':
            with open('NotesDatabase.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(['id', 'title', 'text', 'created', 'modified'])
                for note in unique_notes:
                    writer.writerow([note['id'], note['title'], note['text'], note['created'], note['modified']])
        else:
            raise ValueError(texts.unsupported_file_format, {file_ext})

    def load_from_file(self, file_name):
        """Метод для загрузки заметок из файла."""
        notes = []
        file_ext = os.path.splitext(file_name)[1]
        if file_ext == ".csv":
            with open(file_name, 'rb') as f:
                result = chardet.detect(f.read())
                file_encoding = result['encoding']
            with open(file_name, newline='', encoding=file_encoding) as f:
                reader = csv.reader(f, delimiter=";")
                next(reader)
                for row in reader:
                    created_date = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
                    updated_date = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
                    notes.append(
                        Note(id=row[0], title=row[1], text=row[2], created=created_date, modified=updated_date))
        else:
            raise ValueError(texts.unsupported_file_format, {file_ext})
        return notes
