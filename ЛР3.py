class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Pages should be a positive integer.")

    def __str__(self):
        return f"PaperBook: {self._name} by {self._author}, {self._pages} pages"

    def __repr__(self):
        return f"PaperBook('{self._name}', '{self._author}', {self._pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float) and value > 0:
            self._duration = value
        else:
            raise ValueError("Duration should be a positive float.")

    def __str__(self):
        return f"AudioBook: {self._name} by {self._author}, duration: {self._duration} hours"

    def __repr__(self):
        return f"AudioBook('{self._name}', '{self._author}', {self._duration})"