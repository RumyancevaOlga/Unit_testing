# Представьте, что вы работаете над разработкой простого приложения для записной книжки,
# которое позволяет пользователям добавлять, редактировать и удалять контакты.

from contact import Contact


class Notebook:

    list_notebook = []
    contact_id = 0

    def add_contact(self, telephone: int, name: str, surname: str = None):
        self.contact_id += 1
        contact = Contact(telephone, name, surname, self.contact_id)
        self.list_notebook.append(contact)

    def delete_contact_by_id(self, contact_id):
        for contact in self.list_notebook:
            if contact.contact_id == contact_id:
                return self.list_notebook.remove(contact)
        raise RuntimeError(f'Не существует контакта с id = {contact_id}')

    def edit_contact_by_id(self, contact_id, telephone: int, name: str, surname: str = None):
        for contact in self.list_notebook:
            if contact.contact_id == contact_id:
                self.list_notebook.remove(contact)
                contact = Contact(telephone, name, surname, contact_id)
                return self.list_notebook.append(contact)
        raise RuntimeError(f'Не существует контакта с id = {contact_id}')
    
    def __str__(self):
        return f'{self.list_notebook}'
