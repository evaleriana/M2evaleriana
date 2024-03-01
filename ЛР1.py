mport doctest

class Apple:
    def __init__(self, color: str, weight: float):
        """
        Создание и подготовка к работе объекта "Яблоко"
        :param color: Цвет яблока
        :param weight: Вес яблока в граммах
        Примеры:
        >>> apple = Apple("red", 150)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет яблока должен быть строкой")
        self.color = color

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес яблока должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес яблока должен быть положительным числом")
        self.weight = weight

    def is_ripe(self) -> bool:
        """
        Функция, которая проверяет, спелое ли яблоко
        :return: Является ли яблоко спелым
        Примеры:
        >>> apple = Apple("red", 150)
        >>> apple.is_ripe()
        True
        >>> unripe_apple = Apple("green", 200)
        >>> unripe_apple.is_ripe()
        False
        """
        return self.color.lower() == "red"  # Предположим, что спелые яблоки всегда красные

    def eat(self, bites: int) -> str:
        """
        Метод для поедания яблока.
        :param bites: Количество откушенных кусочков
        :return: Сообщение о том, сколько кусочков было откушено
        Примеры:
        >>> apple = Apple("red", 150)
        >>> apple.eat(3)
        'Откушено 3 кусочка яблока.'
        """
        if not isinstance(bites, int) or bites <= 0:
            raise ValueError("Количество откушенных кусочков должно быть положительным целым числом")
        return f"Откушено {bites} кусочка яблока."


class Tree:
    def __init__(self, age: int, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"
        :param age: Возраст дерева в годах
        :param height: Высота дерева в метрах
        Примеры:
        >>> tree = Tree(5, 2.5)  # инициализация экземпляра класса
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст дерева должен быть положительным целым числом")
        self.age = age

        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

    def grow(self, years: int):
        """
        Метод для роста дерева.
        :param years: Количество лет, на которое дерево должно вырасти
        Примеры:
        >>> tree = Tree(5, 2.5)
        >>> tree.grow(3)
        >>> tree.age
        8
        """
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Количество лет для роста должно быть положительным целым числом")
        self.age += years


class Orchard:
    def __init__(self, trees: list):
        """
        Создание и подготовка к работе объекта "Сад"
        :param trees: Список деревьев в саду
        Примеры:
        >>> apple_tree = Tree(3, 1.8)
        >>> orchard = Orchard([apple_tree])  # инициализация экземпляра класса
        """
        for tree in trees:
            if not isinstance(tree, Tree):
                raise TypeError("Каждый элемент в списке должен быть объектом класса 'Tree'")
        self.trees = trees

    def harvest(self) -> int:
        """
        Метод для сбора урожая из всех деревьев в саду.
        :return: Общее количество собранных яблок
        Примеры:
        >>> apple_tree_1 = Tree(5, 2.5)
        >>> apple_tree_2 = Tree(6, 3.0)
        >>> orchard = Orchard([apple_tree_1, apple_tree_2])
        >>> orchard.harvest()
        0  # В данном примере деревья еще не достаточно выросли для плодоношения
        """
        total_apples = 0
        for tree in self.trees:
            if tree.age >= 4:  # Предположим, что дерево начинает приносить плоды с 4 лет
                total_apples += 10  # Предположим, что каждое дерево приносит 10 яблок
        return total_apples


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    