from tests.UI_tests.data_test.constants import ErrorMsg
from tests.UI_tests.data_test.creds import AliceContactCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import AddContactPageLocators
from tests.UI_tests.pages.addContact import AddContact


def test_all_fields(driver):

    afs = AddContact(driver, Env.url)
    data = AliceContactCreds.return_contact_info
    afs.enter_data(*data)

    assert afs.is_url_correct(Env.contact_list_url)
    assert afs.convert_to_line(*data) in afs.return_contact_list()


def test_mandatory_fields(driver):

    mf = AddContact(driver, Env.url)
    data = AliceContactCreds.contact_info['first_name'], AliceContactCreds.contact_info['last_name']
    mf.enter_data(*data)

    assert mf.is_url_correct(Env.contact_list_url)
    assert mf.convert_to_line(*data) in mf.return_contact_list()


def test_only_first_name(driver):

    ofn = AddContact(driver, Env.url)
    ofn.enter_data(first_name=AliceContactCreds.contact_info['first_name'])

    assert (ofn.get_error_message
            (AddContactPageLocators.error_message) == ErrorMsg.contact_last_name_error)


def test_only_last_name(driver):

    oln = AddContact(driver, Env.url)
    oln.enter_data(last_name=AliceContactCreds.contact_info['last_name'])

    assert (oln.get_error_message
            (AddContactPageLocators.error_message) == ErrorMsg.contact_first_name_error)


def test_max_length_fields(driver):
    mlf = AddContact(driver, Env.url)
    (fn, ln, email, street1, street2, city,
     state_province, postal_code, country) = (AliceContactCreds.contact_info['first_name'] * 15,
                                              AliceContactCreds.contact_info['last_name'] * 15,
                                              AliceContactCreds.contact_info['email'] * 15,
                                              AliceContactCreds.contact_info['street1'] * 15,
                                              AliceContactCreds.contact_info['street2'] * 15,
                                              AliceContactCreds.contact_info['city'] * 15,
                                              AliceContactCreds.contact_info['state_province'] * 15,
                                              AliceContactCreds.contact_info['postal_code'] * 15,
                                              AliceContactCreds.contact_info['country'] * 15)


    mlf.enter_data(first_name=fn, last_name=ln, email=email, street1=street1,
                   street2=street2, city=city, state_province=state_province,
                   postal_code=postal_code, country=country)

    assert (mlf.get_error_message
            (AddContactPageLocators.error_message) == ErrorMsg.contact_max_len_error(fn, ln, street1, street2,
                                                                                     city, state_province,
                                                                                     postal_code, country))


def test_invalid_birthdate(driver):

    invbir = AddContact(driver, Env.url)
    invbir.enter_data(first_name=AliceContactCreds.contact_info['first_name'],
                      last_name=AliceContactCreds.contact_info['last_name'],
                      birthdate='4045-99-98')

    assert (invbir.get_error_message
            (AddContactPageLocators.error_message) == ErrorMsg.contact_birthdate_error)


def test_invalid_email(driver):
    invema = AddContact(driver, Env.url)
    invema.enter_data(first_name=AliceContactCreds.contact_info['first_name'],
                      last_name=AliceContactCreds.contact_info['last_name'],
                      email=AliceContactCreds.contact_info['email'][:5] + AliceContactCreds.contact_info['email'][6:])

    assert (invema.get_error_message
            (AddContactPageLocators.error_message) == ErrorMsg.contact_email_error)
