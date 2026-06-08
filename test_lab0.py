"""Модуль автоматического тестирования объектной модели."""

import unittest
from lab0 import Book, print_report_screen, delete_book_screen


class TestLibraryCatalog(unittest.TestCase):
    """Тестовый набор для верификации библиотечного каталога."""

    def test_book_structure(self):
        """Тест работы Аналитика: Проверка структуры сущности Book."""
        book = Book("Абобус", "Биба", "Фэнтези", 10, 5)
        self.assertEqual(book.title, "Абобус")
        self.assertEqual(book.copies, 10)
        self.assertEqual(book.available, 5)

    def test_empty_catalog_report(self):
        """Тест работы Тестировщика: Вывод отчета при пустом каталоге."""
        catalog = []
        try:
            print_report_screen(catalog)
            status = True
        except Exception:
            status = False
        self.assertTrue(status)

    def test_delete_book_logic(self):
        """Тест работы Тестировщика: Проверка удаления книги из списка."""
        catalog = [
            Book("Абобус", "Биба", "Фэнтези", 10, 5),
            Book("Амогус", "Боба", "Детектив", 5, 2)
        ]
        # Имитируем ввод пользователя через подмену функции input
        import builtins
        original_input = builtins.input
        builtins.input = lambda _: "Абобус"

        try:
            delete_book_screen(catalog)
            # После удаления книги в каталоге должен остаться 1 элемент
            self.assertEqual(len(catalog), 1)
            self.assertEqual(catalog[0].title, "Амогус")
        finally:
            # Восстанавливаем оригинальную функцию ввода
            builtins.input = original_input


if __name__ == '__main__':
    unittest.main()
