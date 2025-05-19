import dataclasses


@dataclasses.dataclass
class ErrorMsg:
    log_in_error = "Incorrect username or password"
    first_name_error = 'User validation failed: firstName: Path `firstName` is required.'
    last_name_error = 'User validation failed: lastName: Path `lastName` is required.'
    email_error = 'User validation failed: email: Email is invalid'
    password_error = 'User validation failed: password: Path `password` is required.'
    alreem_error = 'Email address is already in use'

    contact_first_name_error = "Contact validation failed: firstName: Path `firstName` is required."
    contact_last_name_error = "Contact validation failed: lastName: Path `lastName` is required."


    @staticmethod
    def max_len_error(fn, ln, pw):
        return f"User validation failed: "\
        f"firstName: Path `firstName` (`{fn}`) is longer than the maximum allowed length (20)., "\
        f"lastName: Path `lastName` (`{ln}`) is longer than the maximum allowed length (20)., "\
        f"email: Email is invalid, "\
        f"password: Path `password` (`{pw}`) is longer than the maximum allowed length (100)."


@dataclasses.dataclass
class StringsPage:
    headers_contact_list = ["Name", "Birthdate", "Email", "Phone", "Address",
                            "City, State/Province, Postal Code", "Country"]
    title = 'Contact List App'
