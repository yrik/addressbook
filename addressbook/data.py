class AddressBook(object):
    """
    Class that implements AddressBook storage/retrieval actions

    Assumptions:
        An address book is a collection of persons and groups.

        A person has a first name and a last name.
        A person has one or more street addresses.
        A person has one or more email addresses.
        A person has one or more phone numbers.
        A person can be a member of one or more groups.
    """

    groups = ()
    persons = ()

    def add_person(self, person_dict):
        """
        Adds person to collection
        """
        person = self.validate_person(person_dict)
        self.persons = self.persons + (person,)

        for group in person['group_list']:
            self.add_group(group)

        return True

    def add_group(self, group):
        """
        Adds group to collection
        """
        group = self.validate_group(group)
        if group not in self.groups:
            self.groups = self.groups + (group,)
        return True

    def find_persons(self, first_name=None, last_name=None, email=None, group=None):
        """
            Returns list of person that match search query,
            can be given any combination of input args
        """
        result = []
        for person in self.persons:
            is_found = True

            if first_name and person['first_name'] != first_name:
                is_found = False

            if last_name and person['last_name'] != last_name:
                is_found = False

            if group and group not in person['group_list']:
                is_found = False

            if email:
                if not bool(filter(lambda x: x.startswith(email), person['email_list'])):
                    is_found = False

            if is_found:
                result.append(person)

        return result

    def validate_person(self, person_dict):

        self.__check_string(person_dict, 'first_name')
        self.__check_string(person_dict, 'last_name')

        self.__check_list_of_strings(person_dict, 'address_list')
        self.__check_list_of_strings(person_dict, 'phone_list')
        self.__check_list_of_strings(person_dict, 'email_list')
        self.__check_list_of_strings(person_dict, 'group_list', min_length=0)

        return {
            'first_name': person_dict.get('first_name'),
            'last_name': person_dict.get('last_name'),
            'address_list': person_dict.get('address_list'),
            'phone_list': person_dict.get('phone_list'),
            'email_list': person_dict.get('email_list'),
            'group_list': person_dict.get('group_list'),
        }

    def validate_group(self, group):
        self.__check_string({'group': group}, 'group')
        return group

    def __check_string(self, data, key):

        value = data.get(key)
        if not isinstance(value, basestring):
            raise ValueError(
                '{} is required and must be valid string'.format(key)
            )
        return value

    def __check_list_of_strings(self, data, key, min_length=1):

        values_list = data.get(key)
        if not isinstance(values_list, list):
            raise ValueError(
                '{} is required and must be valid list'.format(key)
            )

        if len(values_list) < min_length:
            raise ValueError(
                '{} must contain at least {} value'.format(key, min_length)
            )

        for value in values_list:
            if not isinstance(value, basestring):
                raise ValueError(
                    '{} must must contain valid strings'.format(key)
                )
        return values_list
