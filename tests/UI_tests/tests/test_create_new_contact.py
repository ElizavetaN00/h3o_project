import pytest

from tests.UI_tests.data_test.constants import ErrorMsg
from tests.UI_tests.data_test.creds import ContactCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import AddContactPageLocators
from tests.UI_tests.pages.add_contact import AddContact


@pytest.mark.test_create_new_contact
@pytest.mark.contact_management
class TestCreateNewContact:

    @pytest.mark.critical_path
    @pytest.mark.acceptance
    def test_all_fields(self, driver):

        afs = AddContact(driver, Env.url)
        data = ContactCreds.return_alice_contact_info
        afs.enter_new_contact()

        assert afs.is_url_correct(Env.contact_list_url)
        assert afs.convert_to_line(*data) in afs.return_contact_list()


    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.aceptance
    def test_mandatory_fields(self, driver):

        mf = AddContact(driver, Env.url)
        data = ContactCreds.alice_contact_info['first_name'], ContactCreds.alice_contact_info['last_name']
        mf.enter_new_contact()

        assert mf.is_url_correct(Env.contact_list_url)
        assert mf.convert_to_line(*data) in mf.return_contact_list()


    @pytest.mark.critical_path
    def test_only_first_name(self, driver):

        ofn = AddContact(driver, Env.url)
        ofn.enter_new_contact(first_name=ContactCreds.alice_contact_info['first_name'])

        assert (ofn.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_last_name_error)

    @pytest.mark.regression
    def test_only_last_name(self, driver):

        oln = AddContact(driver, Env.url)
        oln.enter_new_contact(last_name=ContactCreds.alice_contact_info['last_name'])

        assert (oln.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_first_name_error)


    @pytest.mark.regression
    def test_max_length_fields(self, driver):
        mlf = AddContact(driver, Env.url)
        (fn, ln, email, street1, street2, city,
         state_province, postal_code, country) = (ContactCreds.alice_contact_info['first_name'] * 15,
                                                  ContactCreds.alice_contact_info['last_name'] * 15,
                                                  ContactCreds.alice_contact_info['email'] * 15,
                                                  ContactCreds.alice_contact_info['street1'] * 15,
                                                  ContactCreds.alice_contact_info['street2'] * 15,
                                                  ContactCreds.alice_contact_info['city'] * 15,
                                                  ContactCreds.alice_contact_info['state_province'] * 15,
                                                  ContactCreds.alice_contact_info['postal_code'] * 15,
                                                  ContactCreds.alice_contact_info['country'] * 15)

        mlf.enter_new_contact(first_name=fn, last_name=ln, email=email, street1=street1, street2=street2, city=city,
                              state_province=state_province, postal_code=postal_code, country=country)

        assert (mlf.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_max_len_error(fn, ln, street1, street2,
                                                                                         city, state_province,
                                                                                         postal_code, country))

    @pytest.mark.regression
    def test_invalid_birthdate(self, driver):

        invbir = AddContact(driver, Env.url)
        invbir.enter_new_contact(first_name=ContactCreds.alice_contact_info['first_name'],
                                 last_name=ContactCreds.alice_contact_info['last_name'], birthdate='4045-99-98')

        assert (invbir.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_birthdate_error)


    @pytest.mark.regression
    def test_invalid_email(self, driver):
        invema = AddContact(driver, Env.url)
        invema.enter_new_contact(first_name=ContactCreds.alice_contact_info['first_name'],
                                 last_name=ContactCreds.alice_contact_info['last_name'],
                                 email=ContactCreds.alice_contact_info['email'][:5] +
                                       ContactCreds.alice_contact_info['email'][6:])

        assert (invema.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_email_error)


    @pytest.mark.aceptance
    def test_special_symbol(self, driver):
        specsym = AddContact(driver, Env.url)
        fn, ln, e, p, s1, s2, c, sp, cn = ContactCreds.special_symbol_contact_info['first_name'], ContactCreds.special_symbol_contact_info['last_name'], \
                                    ContactCreds.special_symbol_contact_info['email'], ContactCreds.special_symbol_contact_info['phone'], \
                            ContactCreds.special_symbol_contact_info['street1'], ContactCreds.special_symbol_contact_info['street2'], \
                            ContactCreds.special_symbol_contact_info['city'], ContactCreds.special_symbol_contact_info['state_province'], \
                    ContactCreds.special_symbol_contact_info['country']

        specsym.enter_new_contact(first_name=fn, last_name=ln, email=e, phone=p, street1=s1, street2=s2, city=c,
                                  state_province=sp, country=cn)

        assert specsym.convert_to_line(first_name=fn, last_name=ln, email=e, phone=p, street1=s1, street2=s2,
                                       city=c, state_province=sp, country=cn) in specsym.return_contact_list()


    @pytest.mark.regression
    def test_emoji(self, driver):
        emoji = AddContact(driver, Env.url)
        fn, ln, s1, s2, c, sp, cn = ContactCreds.emoji_contact_info['first_name'], ContactCreds.emoji_contact_info['last_name'], \
                                    ContactCreds.emoji_contact_info['street1'], ContactCreds.emoji_contact_info['street2'], \
                                    ContactCreds.emoji_contact_info['city'], ContactCreds.emoji_contact_info['state_province'], \
                                    ContactCreds.emoji_contact_info['country']
        emoji.enter_new_contact(first_name=fn, last_name=ln, street1=s1, street2=s2, city=c, state_province=sp,
                                country=cn)

        assert emoji.convert_to_line(first_name=fn, last_name=ln, street1=s1, street2=s2,
                                     city=c, state_province=sp, country=cn) in emoji.return_contact_list()
