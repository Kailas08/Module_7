import os
import time

# Задайте путь к каталогу
directory = os.getcwd()

# Проверка существования каталога
if not os.path.exists(directory):
    print(f"Каталог {directory} не существует.")
else:
    # Обход каталога с использованием os.walk
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Формируем полный путь к файлу
            filepath = os.path.join(root, file)

            # Получаем время последнего изменения файла
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            # Получаем размер файла
            filesize = os.path.getsize(filepath)

            # Получаем родительскую директорию файла
            parent_dir = os.path.dirname(filepath)

            # Вывод информации о файле
            print(f'Обнаружен файл: {file}, '
                  f'Путь: {filepath}, Размер: {filesize} байт, '
                  f'Время изменения: {formatted_time}')