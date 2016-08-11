Address Book storage library
================================
The assignment is to implement a simple address book library in Python.


Basic Usage. API calls examples.
================================

Requirements

- Python 2.7


```python

from addressbook import AddressBook

address_book = AddressBook()


# Add a person to the address book
john_dict = {
    'first_name': 'John',
    'last_name': 'Deer',
    'email_list': ['john@xample.com'],
    'phone_list': ['999-999-9999'],
    'address_list': ['Anthony Benoit 490 E, Main Street Norwich, CT 06360, US'],
    'group_list': ['general'],
}

address_book.add_person(john_dict)

# Add a group to address book
address_book.add_group("friends")

# Find group members
address_book.find_persons(group='general')

# Find person using first_name only
address_book.find_persons(first_name='John')

# Find person using first_name and last_name
address_book.find_persons(first_name='John', last_name='Deer')

# Find person using email
address_book.find_persons(email='john@xample.com')

# Find person using email prefix
address_book.find_persons(email='john')

```