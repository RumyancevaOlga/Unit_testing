from notebook import Notebook


class UserInterface:

    def __init__(self, notebook: Notebook):
        self._notebook = notebook

    @property
    def notebook(self):
        return self._notebook

    def add_contact(self, telephone: int, name: str, surname: str = None):
        self._notebook.add_contact(telephone, name, surname)

    def delete_contact_by_id(self, contact_id):
        self._notebook.delete_contact_by_id(contact_id)

    def edit_contact_by_id(self, contact_id, telephone: int, name: str, surname: str = None):
        self._notebook.edit_contact_by_id(contact_id, telephone, name, surname)
