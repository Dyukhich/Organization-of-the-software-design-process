"""Модуль автоматического тестирования объектной модели."""

import unittest
from lab0 import Book, print_report_screen


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


if __name__ == '__main__':
    unittest.main()
