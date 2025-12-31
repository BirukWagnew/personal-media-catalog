from abc import ABC

class Media(ABC):
    def __init__(self, title, year, creator, extra):
        self.title = title
        self.year = year
        self.creator = creator
        self.extra = extra

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.creator}"
