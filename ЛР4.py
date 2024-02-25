class Animal:
    """
    Base class representing an animal.
    Attributes:
        name (str): The name of the animal.
    """

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        """
        Method to make the animal speak.
        Returns:
            str: A greeting message from the animal.
        """
        return f"{self.name} says Hello!"


class Dog(Animal):
    """
    Class representing a Dog, inheriting from Animal.
    Attributes:
        breed (str): The breed of the dog.
    """

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        """
        Method to make the dog speak.
        Returns:
            str: A barking message from the dog.
        """
        return f"{self.name} the {self.breed} barks: Woof! Woof!"

    def fetch(self, item: str) -> str:
        """
        Method to make the dog fetch an item.
        Args:
            item (str): The item to fetch.
        Returns:
            str: A message confirming the item fetched.
        """
        return f"{self.name} fetched the {item}!"


class Cat(Animal):
    """
    Class representing a Cat, inheriting from Animal.
    Attributes:
        color (str): The color of the cat.
    """

    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    def speak(self) -> str:
        """
        Method to make the cat speak.
        Returns:
            str: A meowing message from the cat.
        """
        return f"{self.name} the {self.color} cat meows: Meow! Meow!"

    def sleep(self) -> str:
        """
        Method to make the cat sleep.
        Returns:
            str: A message indicating the cat is sleeping.
        """
        return f"{self.name} is now sleeping peacefully."