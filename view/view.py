from view import texts


def view_notes(notes):
    """
    Метод выводит информацию о всех заметках из экземпляра класса Notes.
    """
    all_notes = notes.read()
    if all_notes:
        print(texts.all_list)
        for note in all_notes:
            print(f"ID: {note.id},"
                  f"Заголовок: {note.title},"
                  f"Текст: {note.text},"
                  f"Создан: {note.created.strftime('%Y-%m-%d %H:%M:%S')},"
                  f"Изменен: {note.modified.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(texts.empty_list)
