import unittest
from main import Color, Circle, Rectangle, Triangle, ShapeFactory, ProgramEngine

class TestShapeDesign(unittest.TestCase):
    """Тестовый набор для проверки объектной модели геометрических фигур."""

    def test_color_enum_valid(self):
        """Тест: Корректное распознавание существующих цветов."""
        self.assertEqual(Color.from_string("Красный"), Color.RED)
        self.assertEqual(Color.from_string("Blue"), Color.BLUE)

    def test_color_enum_invalid(self):
        """Тест: Обработка неизвестного цвета."""
        self.assertEqual(Color.from_string("Розовый"), Color.UNKNOWN)

    def test_circle_creation(self):
        """Тест: Успешное создание круга и проверка свойств."""
        circle = Circle(cx=10, cy=20, r=5, c=Color.RED, date="2026-06-08")
        self.assertEqual(circle.get_type_str(), "Круг")
        self.assertEqual(circle.radius, 5)


class TestShapeFactory(unittest.TestCase):
    """Тестовый набор для проверки фабрики объектов и исключительных ситуаций."""

    def test_factory_success_rect(self):
        """Тест: Успешное создание прямоугольника фабрикой."""
        parts = ["ADD", "RECT", "1.5", "2.5", "4.0", "6.0", "Синий", "2026-05-12"]
        shape = ShapeFactory.create_shape(parts)
        self.assertIsNotNone(shape)
        self.assertEqual(shape.get_type_str(), "Прямоугольник")

    def test_factory_invalid_types(self):
        """Тест: Исключительная ситуация — некорректный тип данных (строка вместо чисел)."""
        parts = ["ADD", "CIRCLE", "not_a_number", "20", "5", "Красный", "2026-06-08"]
        shape = ShapeFactory.create_shape(parts)
        self.assertIsNone(shape)  # Фабрика должна поймать ValueError и вернуть None

    def test_factory_index_error(self):
        """Тест: Исключительная ситуация — нехватка аргументов в строке."""
        parts = ["ADD", "TRIANGLE", "0", "0", "Зеленый"]  # Мало координат
        shape = ShapeFactory.create_shape(parts)
        self.assertIsNone(shape)  # Фабрика должна поймать IndexError и вернуть None


class TestProgramEngine(unittest.TestCase):
    """Тестовый набор для проверки логики работы контейнера."""

    def setUp(self):
        """Подготовка чистого движка перед каждым тестом."""
        self.engine = ProgramEngine()

    def test_engine_rem_by_color(self):
        """Тест: Удаление элементов из контейнера по цвету."""
        self.engine.container.append(Circle(0, 0, 5, Color.RED, "2026"))
        self.engine.container.append(Rectangle(1, 1, 2, 2, Color.BLUE, "2026"))
        
        self.engine._execute_rem("color=Красный")
        self.assertEqual(len(self.engine.container), 1)
        self.assertEqual(self.engine.container[0].get_type_str(), "Прямоугольник")

    def test_engine_rem_by_type(self):
        """Тест: Удаление элементов из контейнера по типу фигуры."""
        self.engine.container.append(Circle(0, 0, 5, Color.RED, "2026"))
        self.engine.container.append(Triangle(0,0,1,1,2,2, Color.GREEN, "2026"))
        
        self.engine._execute_rem("type=Круг")
        self.assertEqual(len(self.engine.container), 1)
        self.assertEqual(self.engine.container[0].get_type_str(), "Треугольник")


if __name__ == "__main__":
    unittest.main()
