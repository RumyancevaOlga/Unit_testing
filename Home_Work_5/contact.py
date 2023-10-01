class Contact:

    def __init__(self, telephone: int, name: str, surname: str = None, contact_id: int = None):
        self._contact_id = contact_id
        self._telephone = telephone
        self._name = name
        self._surname = surname

    @property
    def contact_id(self):
        return self._contact_id

    @property
    def telephone(self):
        return self._telephone

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    def __str__(self):
        return f'{self._name} {self._surname} {self._telephone}'

    def __repr__(self):
        return f'Contact({self._telephone}, {self._name}, {self._surname})'

    def __eq__(self, other):
        return self._contact_id == other.contact_id
