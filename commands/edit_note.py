class EditNoteCommand:
    """Класс для редактирования заметки"""

    def __init__(self, notes, id, title=None, text=None):
        """Конструктор класса EditNoteCommand
        notes - объект класса Notes, с которым команда работает,
        id - идентификатор заметки,
        title - новый заголовок заметки,
        text - новый текст заметки.
        """
        self.notes = notes
        self.id = id
        self.title = title
        self.text = text

    def execute(self):
        """Метод выполнения команды edit"""
        self.notes.edit(self.id, self.title, self.text)
