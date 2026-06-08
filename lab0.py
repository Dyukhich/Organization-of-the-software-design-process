"""Программа: Управление библиотечным каталогом (v2.0).

Описание: Ведет учет книг, выводит отчеты.
Язык: Python 3
"""


class Book:
    """Структура для хранения информации о книге."""

    def __init__(self, title: str, author: str, genre: str,
                 copies: int, available: int):
        """Инициализация объекта книги."""
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies
        self.available = available


def add_book_screen(catalog):
    """Экран интерактивного добавления новой книги в каталог."""
    print("\n--- Ввод данных о новой книге ---")
    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    genre = input("Введите жанр книги: ").strip()

    while True:
        try:
            copies = int(input("Введите общее количество экземпляров: "))
            if copies < 0:
                print("Количество не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    while True:
        try:
            available = int(input("Введите количество доступных книг: "))
            if available < 0:
                print("Количество не может быть отрицательным!")
                continue
            if available > copies:
                print(f"Доступных книг не может быть больше ({copies})!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    new_book = Book(title, author, genre, copies, available)
    catalog.append(new_book)
    print(f"Успешно добавлено: «{title}»")


def print_report_screen(catalog):
    """Экран вывода итогового аналитического отчета по всему каталогу."""
    if not catalog:
        print("\n[Каталог пуст. Сначала добавьте книги через меню]")
        return

    total_books_types = len(catalog)
    total_copies_in_library = sum(book.copies for book in catalog)
    total_available_books = sum(book.available for book in catalog)

    print("\n" + "=" * 50)
    print("ИТОГОВЫЙ ОТЧЕТ ПО БИБЛИОТЕЧНОМУ КАТАЛОГУ")
    print("=" * 50)

    for idx, book in enumerate(catalog, 1):
        print(f"{idx}. «{book.title}» — {book.author} [{book.genre}]")
        print(f"   Всего: {book.copies} шт. | На полках: {book.available} шт.")

    print("-" * 50)
    print(f"Всего наименований книг в каталоге: {total_books_types}")
    print(f"Общее количество экземпляров всех книг: {total_copies_in_library}")
    print(f"Всего доступно к выдаче прямо сейчас: {total_available_books}")
    print("=" * 50)


def main():
    """Главная функция управления интерактивным меню библиотеки."""
    catalog = []

    while True:
        print("\n" + "=" * 40)
        print("       ГЛАВНОЕ МЕНЮ БИБЛИОТЕКИ")
        print("=" * 40)
        print("1. Добавить новую книгу в каталог")
        print("2. Сформировать итоговый отчет")
        print("3. Выйти из программы")
        print("-" * 40)

        choice = input("Выберите действие (1-3): ").strip()

        if choice == "1":
            add_book_screen(catalog)
        elif choice == "2":
            print_report_screen(catalog)
        elif choice == "3":
            print("\nЗавершение работы системы. До свидания!")
            print("=" * 40)
            break
        else:
            print("\nОшибка! Некорректный пункт меню.")


if __name__ == "__main__":
    main()
