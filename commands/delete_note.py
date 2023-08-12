class DeleteNoteCommand:
    """Класс для удаления заметки"""

    def __init__(self, notes, id):
        """Конструктор класса DeleteNoteCommand
        notes - объект класса Notes, с которым команда работает,
        id - идентификатор заметки.
        """
        self.notes = notes
        self.id = id

    def execute(self):
        """Метод выполнения команды delete"""
        self.notes.delete(self.id)
