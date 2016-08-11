import unittest

from addressbook import AddressBook


class TestAddressBookApiMethods(unittest.TestCase):

    def setUp(self):
        self.address_book = AddressBook()

    def test_add_person(self):

        self.assertRaises(ValueError, self.address_book.add_person, {})

        person_dict = {
            'first_name': 'John',
            'last_name': 'Deer',
            'email_list': ['john@xample.com'],
            'phone_list': ['999-999-9999'],
            'address_list': ['Anthony Benoit 490 E, Main Street Norwich, CT 06360, US'],
            'group_list': ['general'],
        }

        result = self.address_book.add_person(person_dict)
        self.assertTrue(result)

    def test_add_group(self):

        self.assertRaises(ValueError, self.address_book.add_group, None)

        result = self.address_book.add_group('general')
        self.assertTrue(result)

    def test_find(self):

        address_book = self.address_book

        john_dict = {
            'first_name': 'John',
            'last_name': 'Deer',
            'email_list': ['john@xample.com'],
            'phone_list': ['999-999-9999'],
            'address_list': ['Anthony Benoit 490 E, Main Street Norwich, CT 06360, US'],
            'group_list': ['general'],
        }
        address_book.add_person(john_dict)

        bob_dict = {
            'first_name': 'Bob',
            'last_name': 'Dilan',
            'email_list': ['bob@example.com', 'bob2@example.com'],
            'phone_list': ['999-888-9999'],
            'address_list': ['Green 490 E, Main Street Norwich, CT 06360, US'],
            'group_list': ['general', 'friends'],
        }
        address_book.add_person(bob_dict)

        result1 = address_book.find_persons(first_name='Bob')
        self.assertEqual(result1, [bob_dict])

        result2 = address_book.find_persons(first_name='Bob', last_name='Dilan')
        self.assertEqual(result2, [bob_dict])

        result3 = address_book.find_persons(email='bob@example.com')
        self.assertEqual(result3, [bob_dict])

        result4 = address_book.find_persons(email='john')
        self.assertEqual(result4, [john_dict])

        result5 = address_book.find_persons(group='general')
        self.assertEqual(result5, [john_dict, bob_dict])


if __name__ == '__main__':
    unittest.main()
