class CreateNoteCommand:
    """Класс для создания заметки"""

    def __init__(self, notes, id, title, text):
        """Конструктор класса CreateNoteCommand.
        notes - объект класса Notes, с которым команда работает,
        id - идентификатор заметки,
        title - заголовок заметки,
        text - текст заметки.
        """
        self.notes = notes
        self.id = id
        self.title = title
        self.text = text

    def execute(self):
        """Метод выполнения команды create"""
        self.notes.create(self.id, self.title, self.text)
