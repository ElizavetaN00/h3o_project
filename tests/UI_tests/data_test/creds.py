import dataclasses
import random
import string


@dataclasses.dataclass
class RegistrationUserCreds:

    @staticmethod
    def gen_str():
        val = list(string.hexdigits)
        random.shuffle(val)
        return ''.join(val)[:9]

    first_name = gen_str()
    last_name = gen_str()
    email = gen_str() + '@gmail.com'
    password = gen_str()


@dataclasses.dataclass
class SimonUserCreds:
    first_name = 'Simon'
    last_name = 'Wilson'
    email = 'simonw@gmail.com'
    password = 'Testsimon4'


@dataclasses.dataclass
class ContactCreds:
    alice_contact_info = {
        "first_name": "Alice",
        "last_name": "Green",
        "birthdate": "1997-08-09",
        "email": "alice@gmail.com",
        "phone": "+16507599755",
        "street1": "1101 Summit St",
        "street2": "244 Aspen Hills Ct",
        "city": "Evanston",
        "state_province": "WY",
        "postal_code": "82930",
        "country": "USA"
    }

    return_alice_contact_info = list(alice_contact_info.values())

    emoji_contact_info = {
        'first_name': 'Alice😉',
        'last_name': '🍇Green',
        'street1': '1101 Summit St😃',
        'street2': '244 Aspen Hills Ct😀',
        'city': '🤯Evanston',
        'state_province': '🍉WY',
        'country': 'USA👾'
    }

    special_symbol_contact_info = {
        'first_name': 'Alíce',
        'last_name': "O'Green",
        'email': 'alíce.s+mít@test.com',
        'phone': '+1(650)7599755',
        'street1': '1101# Summit St',
        'street2': '244$ Aspen Hills Ct',
        'city': '<Evanston>',
        'state_province': '&WY',
        'country': '{USA}'
    }
