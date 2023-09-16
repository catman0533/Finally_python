

import os

def create_note():
    note = input("Введите текст заметки: ")
    file_name = input("Введите название файла для сохранения заметки: ")

    # Проверяем, что файл с таким названием не существует
    if os.path.exists(file_name):
        print("Файл с таким названием уже существует")
        return
    
    with open(file_name, 'w') as file:
        file.write(note)
    
    print("Заметка успешно создана")

def read_notes():
    notes = os.listdir()

    # Фильтруем только файлы с расширением .txt
    notes = [note for note in notes if note.endswith(".txt")]

    if not notes:
        print("Заметки не найдены")
        return
    
    print("Список заметок:")
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}")

def edit_note():
    note_name = input("Введите название заметки для редактирования: ")

    # Проверяем, что файл с таким названием существует
    if not os.path.exists(note_name):
        print("Заметка не найдена")
        return

    with open(note_name, 'r') as file:
        note = file.read()
    
    print(f"Текущий текст заметки:\n{note}")

    new_note = input("Введите новый текст заметки: ")

    with open(note_name, 'w') as file:
        file.write(new_note)
    
    print("Заметка успешно отредактирована")

def delete_note():
    note_name = input("Введите название заметки для удаления: ")

    # Проверяем, что файл с таким названием существует
    if not os.path.exists(note_name):
        print("Заметка не найдена")
        return

    os.remove(note_name)

    print("Заметка успешно удалена")

def main():
    while True:
        print("\n=== Меню ===")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор, попробуйте снова")

if __name__ == "__main__":
    main()

