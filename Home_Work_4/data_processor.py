class Database:

    def query(self, sql: str) -> list[str]:
        print(f'Отрабатываю {sql} запрос')
        return ['какой-то', 'список']


class DataProcessor:

    def __init__(self, database: Database):
        self._database = database

    @property
    def database(self):
        return self._database

    def request(self, sql: str) -> None:
        self._database.query(sql)
