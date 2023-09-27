import abc


class BookRepository(abc.ABC):

    def info(self, author: str, title: str):
        pass


class BookService(BookRepository):

    def __init__(self, repository):
        self._repository = repository

    def info(self, author: str, title: str):
        return f'Информация о книге "{title}" автора {author}'
