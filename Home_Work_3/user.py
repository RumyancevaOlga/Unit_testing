class User:

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._is_authenticate = False
        self._is_admin = False

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def is_authenticate(self):
        return self._is_authenticate

    @property
    def is_admin(self):
        return self._is_admin

    def add_admin(self):
        self._is_admin = True

    def authenticate(self, login: str, password: str) -> bool:
        self._is_authenticate = self._login == login and self.password == password
        return self._is_authenticate

    def __repr__(self):
        return f'User({self._login}, {self._password})'

    def __eq__(self, other):
        return self._login == other.login and self.password == other.password
