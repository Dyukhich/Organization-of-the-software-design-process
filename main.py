from enum import Enum
from typing import List, Optional


class Color(Enum):
    """Перечисление допустимых цветов геометрических фигур."""
    RED = "Красный"
    ORANGE = "Оранжевый"
    YELLOW = "Желтый"
    GREEN = "Зеленый"
    CYAN = "Голубой"
    BLUE = "Синий"
    PURPLE = "Фиолетовый"
    UNKNOWN = "Неизвестный"

    @classmethod
    def from_string(cls, name: str) -> "Color":
        """Фабричный метод преобразования текстовой строки в объект Color."""
        mapping = {
            "Красный": cls.RED, "Red": cls.RED,
            "Оранжевый": cls.ORANGE, "Orange": cls.ORANGE,
            "Желтый": cls.YELLOW, "Yellow": cls.YELLOW,
            "Зеленый": cls.GREEN, "Green": cls.GREEN,
            "Голубой": cls.CYAN, "Cyan": cls.CYAN,
            "Синий": cls.BLUE, "Blue": cls.BLUE,
            "Фиолетовый": cls.PURPLE, "Purple": cls.PURPLE
        }
        return mapping.get(name, cls.UNKNOWN)


class Shape:
    """Абстрактный базовый класс для всех типов плоских фигур."""
    def __init__(self, color: Color, last_modified: str):
        self.color = color
        self.last_modified = last_modified

    def print_info(self) -> None:
        """Полиморфный метод вывода полной информации об объекте."""
        raise NotImplementedError

    def get_type_str(self) -> str:
        """Возвращает строгое текстовое имя типа фигуры."""
        raise NotImplementedError


class Circle(Shape):
    """Класс геометрической фигуры 'Круг'."""
    def __init__(self, cx: int, cy: int, r: int, c: Color, date: str):
        super().__init__(c, date)
        self.cx = cx
        self.cy = cy
        self.radius = r

    def print_info(self) -> None:
        print(f"[Круг] Центр: ({self.cx}, {self.cy}), "
              f"Радиус: {self.radius} | Цвет: {self.color.value} | "
              f"Дата изменения: {self.last_modified}")

    def get_type_str(self) -> str:
        return "Круг"


class Rectangle(Shape):
    """Класс геометрической фигуры 'Прямоугольник'."""
    def __init__(self, x1: float, y1: float, x2: float, y2: float,
                 c: Color, date: str):
        super().__init__(c, date)
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def print_info(self) -> None:
        print(f"[Прямоугольник] ЛВ: ({self.x1}, {self.y1}), "
              f"ПН: ({self.x2}, {self.y2}) | Цвет: {self.color.value} | "
              f"Дата изменения: {self.last_modified}")

    def get_type_str(self) -> str:
        return "Прямоугольник"


class Triangle(Shape):
    """Класс геометрической фигуры 'Треугольник'."""
    def __init__(self, x1: float, y1: float, x2: float, y2: float,
                 x3: float, y3: float, c: Color, date: str):
        super().__init__(c, date)
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def print_info(self) -> None:
        print(f"[Треугольник] Точки: ({self.x1},{self.y1}), "
              f"({self.x2},{self.y2}), ({self.x3},{self.y3}) | "
              f"Цвет: {self.color.value} | "
              f"Дата изменения: {self.last_modified}")

    def get_type_str(self) -> str:
        return "Треугольник"


class ShapeFactory:
    """Фабрика для безопасного создания объектов фигур."""
    @staticmethod
    def create_shape(parts: List[str]) -> Optional[Shape]:
        """Парсит аргументы строки и возвращает объект Shape."""
        try:
            shape_type = parts[1]
            if shape_type == "CIRCLE":
                return Circle(int(parts[2]), int(parts[3]), int(parts[4]),
                              Color.from_string(parts[5]), parts[6])
            elif shape_type == "RECT":
                return Rectangle(float(parts[2]), float(parts[3]),
                                 float(parts[4]), float(parts[5]),
                                 Color.from_string(parts[6]), parts[7])
            elif shape_type == "TRIANGLE":
                return Triangle(float(parts[2]), float(parts[3]),
                                float(parts[4]), float(parts[5]),
                                float(parts[6]), float(parts[7]),
                                Color.from_string(parts[8]), parts[9])
        except (IndexError, ValueError) as e:
            print(f"Ошибка синтаксиса при добавлении фигуры: {e}")
        return None


class ProgramEngine:
    """Главный управляющий класс для работы с контейнером фигур."""
    def __init__(self):
        self.container: List[Shape] = []

    def _execute_rem(self, condition: str) -> None:
        if '=' not in condition:
            return
        key, value = condition.split('=', 1)
        initial_count = len(self.container)

        if key == "color":
            self.container = list(
                filter(lambda s: s.color.value != value, self.container)
            )
        elif key == "type":
            self.container = list(
                filter(lambda s: s.get_type_str() != value, self.container)
            )

        if len(self.container) < initial_count:
            print(f">>> Выполнено удаление по условию: {condition}")

    def process_file(self, filename: str) -> None:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    command = parts[0]

                    if command == "ADD":
                        new_shape = ShapeFactory.create_shape(parts)
                        if new_shape:
                            self.container.append(new_shape)
                    elif command == "REM":
                        self._execute_rem(parts[1])
                    elif command == "PRINT":
                        print("--- Содержимое контейнера ---")
                        if not self.container:
                            print("[Контейнер пуст]")
                        else:
                            for shape in self.container:
                                shape.print_info()
                        print("-----------------------------")
        except FileNotFoundError:
            print(f"Ошибка: Файл {filename} не найден.")


if __name__ == "__main__":
    engine = ProgramEngine()
    engine.process_file("commands.txt")
