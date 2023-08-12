import os

from view import texts


def list_files():
    """Функция для отображения списка файлов в текущей директории
    file - имя файла"""
    files = [file for file in os.listdir('.') if os.path.isfile(file)]
    print(texts.file_list)
    for file in files:
        print(file)
