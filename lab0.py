"""
Программа: Управление библиотечным каталогом
Описание: Позволяет вводить данные о книгах и рассчитывать их общее количество.
Язык: Python 3
"""

class Book:
    """Структура для хранения информации о книге."""
    def __init__(self, title: str, author: str, genre: str, copies: int, available: int):
        self.title = title          # Название книги
        self.author = author        # Автор книги
        self.genre = genre          # Жанр
        self.copies = copies        # Количество экземпляров (всего)
        self.available = available  # Общее количество доступных книг прямо сейчас


def main():
    print("=" * 50)
    print("СИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕЧНЫМ КАТАЛОГОМ")
    print("=" * 50)

    catalog = []  # Список для хранения структуры книг

    # Цикл для ввода данных о нескольких книгах
    while True:
        print("\n--- Ввод данных о новой книге ---")
        title = input("Введите название книги: ").strip()
        author = input("Введите автора книги: ").strip()
        genre = input("Введите жанр книги: ").strip()

        # Валидация числового ввода для общего количества экземпляров
        while True:
            try:
                copies = int(input("Введите общее количество экземпляров: "))
                if copies < 0:
                    print("Количество не может быть отрицательным!")
                    continue
                break
            except ValueError:
                print("Ошибка! Введите целое число.")

        # Валидация числового ввода для доступных книг
        while True:
            try:
                available = int(input("Введите количество доступных книг на полках: "))
                if available < 0:
                    print("Количество не может быть отрицательным!")
                    continue
                if available > copies:
                    print(f"Доступных книг не может быть больше, чем всего экземпляров ({copies})!")
                    continue
                break
            except ValueError:
                print("Ошибка! Введите целое число.")

        # Создаем объект книги и добавляем его в каталог
        new_book = Book(title, author, genre, copies, available)
        catalog.append(new_book)

        # Запрос на продолжение ввода
        proceed = input("\nХотите добавить еще одну книгу? (да/нет): ").strip().lower()
        if proceed not in ['да', 'д', 'yes', 'y']:
            break

    # Расчет итоговых показателей системы
    total_books_types = len(catalog)
    total_copies_in_library = sum(book.copies for book in catalog)
    total_available_books = sum(book.available for book in catalog)

    # Вывод итоговой информации каталога
    print("\n" + "=" * 50)
    print("ИТОГОВЫЙ ОТЧЕТ ПО БИБЛИОТЕЧНОМУ КАТАЛОГУ")
    print("=" * 50)
    
    for idx, book in enumerate(catalog, 1):
        print(f"{idx}. «{book.title}» — {book.author} [{book.genre}]")
        print(f"   Всего экземпляров: {book.copies} шт. | Доступно на полках: {book.available} шт.")
    
    print("-" * 50)
    print(f"Всего наименований книг в каталоге: {total_books_types}")
    print(f"Общее количество экземпляров всех книг в библиотеке: {total_copies_in_library} шт.")
    print(f"Всего доступно к выдаче прямо сейчас: {total_available_books} шт.")
    print("=" * 50)


if __name__ == "__main__":
    main()
