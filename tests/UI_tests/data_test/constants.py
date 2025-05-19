import dataclasses


@dataclasses.dataclass
class ErrorMsg:
    log_in_error = "Incorrect username or password"
    first_name_error = 'User validation failed: firstName: Path `firstName` is required.'
    last_name_error = 'User validation failed: lastName: Path `lastName` is required.'
    email_error = 'User validation failed: email: Email is invalid'
    password_error = 'User validation failed: password: Path `password` is required.'
    alreem_error = 'Email address is already in use'

    @staticmethod
    def max_len_error(fn, ln, pw):
        return f"User validation failed: "\
        f"firstName: Path `firstName` (`{fn}`) is longer than the maximum allowed length (20)., "\
        f"lastName: Path `lastName` (`{ln}`) is longer than the maximum allowed length (20)., "\
        f"email: Email is invalid, "\
        f"password: Path `password` (`{pw}`) is longer than the maximum allowed length (100)."

    contact_first_name_error = "Contact validation failed: firstName: Path `firstName` is required."
    contact_last_name_error = "Contact validation failed: lastName: Path `lastName` is required."

    @staticmethod
    def contact_max_len_error(fn, ln, street1, street2, city, state_province, postal_code, country):
        return (f"Contact validation failed: "
                f"firstName: Path `firstName` (`{fn}`) is longer than the maximum allowed length (20)., "
                f"lastName: Path `lastName` (`{ln}`) is longer than the maximum allowed length (20)., "
                f"email: Email is invalid, "
                f"street1: Path `street1` (`{street1}`) is longer than the maximum allowed length (40)., "
                f"street2: Path `street2` (`{street2}`) is longer than the maximum allowed length (40)., "
                f"city: Path `city` (`{city}`) is longer than the maximum allowed length (40)., "
                f"stateProvince: Path `stateProvince` (`{state_province}`) is longer than the maximum allowed length (20)., "
                f"postalCode: Path `postalCode` (`{postal_code}`) is longer than the maximum allowed length (10)., "
                f"country: Path `country` (`{country}`) is longer than the maximum allowed length (40).")



@dataclasses.dataclass
class StringsPage:
    headers_contact_list = ["Name", "Birthdate", "Email", "Phone", "Address",
                            "City, State/Province, Postal Code", "Country"]
    title = 'Contact List App'
