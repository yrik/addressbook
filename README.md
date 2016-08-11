Address Book storage library
================================
The assignment is to implement a simple address book library in Python.
Read [here](https://github.com/gingerpayments/hiring/blob/master/coding-assignments/python-address-book-assignment/python-address-book-assignment.rst#requirements) about requirements 

Note: it stores all the data in memory,  for future usage it should be extended with DB/File based storage.
In real production case I would use Django Rest Framework and queries to the database to achieve this functionality.


**See answer to design question below**

>Find person by email address (can supply any substring, ie. "comp" should work assuming "alexander@company.com" is an email address in the address book) - discuss how you would implement this without coding the solution.

I would use following check `if 'comp' in "alexander@company.com"` while looking for relevant objects using Python.
In case of database storage email should be indexed column and I will use query `LIKE '%'`.

Basic Usage. API calls examples.
================================

Requirements

- Python 2.7

Installation

```
mkdir testapp
cd testapp
virtualenv env
source env/bin/activate

git clone git@github.com:yrik/addressbook.git
cd addressbook
python setup.py test
pip install .
cd ..
python
from addressbook import AddressBook
```


API call examples.

``` python

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
