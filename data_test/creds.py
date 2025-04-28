import dataclasses
import random
import string


@dataclasses.dataclass
class AddUserCreds:

    @staticmethod
    def gen_str():
        val = list(string.hexdigits)
        random.shuffle(val)
        return ''.join(val)[:9]

    first_name = gen_str()
    last_name = gen_str()
    email = gen_str() + '@gmail.com'
    password = gen_str()
