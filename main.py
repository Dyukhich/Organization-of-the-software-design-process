from enum import Enum
from datetime import datetime


# Перечисление для безопасного хранения фиксированных цветов фигур
class Color(Enum):
    RED = "Красный"
    ORANGE = "Оранжевый"
    YELLOW = "Желтый"
    GREEN = "Зеленый"
    CYAN = "Голубой"
    BLUE = "Синий"
    PURPLE = "Фиолетовый"
    UNKNOWN = "Неизвестный"

    @classmethod
    def from_string(cls, name: str):
        # Словарь для сопоставления строковых названий (RU/EN) с элементами Enum
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


# Абстрактный базовый класс
class Shape:
    def __init__(self, color: Color, last_modified: str):
        self.color = color
        self.last_modified = last_modified

    # Метод обязателен к переопределению в дочерних классах (полиморфизм)
    def print_info(self):
        raise NotImplementedError("Этот метод должен быть переопределен в наследниках")

    def get_type_str(self) -> str:
        raise NotImplementedError("Этот метод должен быть переопределен в наследниках")


class Circle(Shape):
    def __init__(self, cx: int, cy: int, radius: int, color: Color, last_modified: str):
        super().__init__(color, last_modified)  # Инициализация полей базового класса
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def print_info(self):
        print(f"[Круг] Центр: ({self.cx}, {self.cy}), Радиус: {self.radius} | "
              f"Цвет: {self.color.value} | Дата изменения: {self.last_modified}")

    def get_type_str(self) -> str:
        return "Круг"


class Rectangle(Shape):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: Color, last_modified: str):
        super().__init__(color, last_modified)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def print_info(self):
        print(f"[Прямоугольник] ЛВ: ({self.x1}, {self.y1}), ПН: ({self.x2}, {self.y2}) | "
              f"Цвет: {self.color.value} | Дата изменения: {self.last_modified}")

    def get_type_str(self) -> str:
        return "Прямоугольник"


class Triangle(Shape):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, color: Color, last_modified: str):
        super().__init__(color, last_modified)
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def print_info(self):
        print(f"[Треугольник] Точки: ({self.x1},{self.y1}), ({self.x2},{self.y2}), ({self.x3},{self.y3}) | "
              f"Цвет: {self.color.value} | Дата изменения: {self.last_modified}")

    def get_type_str(self) -> str:
        return "Треугольник"


# Управляющий класс (Контейнер и Парсер)
class ProgramEngine:
    def __init__(self):
        self.container = []  # Стандартный список выступает в роли контейнера фигур

    def _execute_rem(self, condition: str):
        if '=' not in condition:
            return
        
        # Разбиваем условие (например, "color=Красный") на ключ и значение
        key, value = condition.split('=', 1)
        initial_count = len(self.container)

        # Фильтрация списка (удаление объектов) с помощью List Comprehension
        if key == "color":
            self.container = [shape for shape in self.container if shape.color.value != value]
        elif key == "type":
            self.container = [shape for shape in self.container if shape.get_type_str() != value]

        if len(self.container) < initial_count:
            print(f">>> Выполнено удаление по условию: {condition}")

    def process_file(self, filename: str):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split()  # Разделение строки по пробелам на аргументы
                    command = parts[0]    # Первый элемент строки — это всегда имя команды

                    if command == "ADD":
                        shape_type = parts[1]  # Второй элемент определяет тип создаваемой фигуры
                        
                        if shape_type == "CIRCLE":
                            # Построчный парсинг параметров согласно индексам в commands.txt
                            cx, cy, radius = int(parts[2]), int(parts[3]), int(parts[4])
                            color = Color.from_string(parts[5])
                            date = parts[6]
                            self.container.append(Circle(cx, cy, radius, color, date))
                        
                        elif shape_type == "RECT":
                            x1, y1, x2, y2 = float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])
                            color = Color.from_string(parts[6])
                            date = parts[7]
                            self.container.append(Rectangle(x1, y1, x2, y2, color, date))
                        
                        elif shape_type == "TRIANGLE":
                            x1, y1 = float(parts[2]), float(parts[3])
                            x2, y2 = float(parts[4]), float(parts[5])
                            x3, y3 = float(parts[6]), float(parts[7])
                            color = Color.from_string(parts[8])
                            date = parts[9]
                            self.container.append(Triangle(x1, y1, x2, y2, x3, y3, color, date))

                    elif command == "REM":
                        condition = parts[1]
                        self._execute_rem(condition)

                    elif command == "PRINT":
                        print("--- Содержимое контейнера ---")
                        if not self.container:
                            print("[Контейнер пуст]")
                        else:
                            for shape in self.container:
                                shape.print_info()  # Полиморфный вызов вывода информации
                        print("-----------------------------")
                        
        except FileNotFoundError:
            print(f"Ошибка: Файл {filename} не найден.")


if __name__ == "__main__":
    engine = ProgramEngine()
    engine.process_file("commands.txt")
