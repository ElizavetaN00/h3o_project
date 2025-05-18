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
