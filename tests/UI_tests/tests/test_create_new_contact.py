import pytest

from tests.UI_tests.data_test.constants import ErrorMsg
from tests.UI_tests.data_test.creds import AliceContactCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.data_test.locators import AddContactPageLocators
from tests.UI_tests.pages.addContact import AddContact


@pytest.mark.test_create_new_contact
@pytest.mark.contact_management
class TestCreateNewContact:

    @pytest.mark.critical_path
    @pytest.mark.acceptance
    def test_all_fields(self, driver):

        afs = AddContact(driver, Env.url)
        data = AliceContactCreds.return_contact_info
        afs.enter_data(*data)

        assert afs.is_url_correct(Env.contact_list_url)
        assert afs.convert_to_line(*data) in afs.return_contact_list()


    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.aceptance
    def test_mandatory_fields(self, driver):

        mf = AddContact(driver, Env.url)
        data = AliceContactCreds.contact_info['first_name'], AliceContactCreds.contact_info['last_name']
        mf.enter_data(*data)

        assert mf.is_url_correct(Env.contact_list_url)
        assert mf.convert_to_line(*data) in mf.return_contact_list()


    @pytest.mark.critical_path
    def test_only_first_name(self, driver):

        ofn = AddContact(driver, Env.url)
        ofn.enter_data(first_name=AliceContactCreds.contact_info['first_name'])

        assert (ofn.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_last_name_error)

    @pytest.mark.regression
    def test_only_last_name(self, driver):

        oln = AddContact(driver, Env.url)
        oln.enter_data(last_name=AliceContactCreds.contact_info['last_name'])

        assert (oln.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_first_name_error)


    @pytest.mark.regression
    def test_max_length_fields(self, driver):
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

    @pytest.mark.regression
    def test_invalid_birthdate(self, driver):

        invbir = AddContact(driver, Env.url)
        invbir.enter_data(first_name=AliceContactCreds.contact_info['first_name'],
                          last_name=AliceContactCreds.contact_info['last_name'],
                          birthdate='4045-99-98')

        assert (invbir.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_birthdate_error)


    @pytest.mark.regression
    def test_invalid_email(self, driver):
        invema = AddContact(driver, Env.url)
        invema.enter_data(first_name=AliceContactCreds.contact_info['first_name'],
                          last_name=AliceContactCreds.contact_info['last_name'],
                          email=AliceContactCreds.contact_info['email'][:5] + AliceContactCreds.contact_info['email'][6:])

        assert (invema.get_error_message
                (AddContactPageLocators.error_message) == ErrorMsg.contact_email_error)


    @pytest.mark.aceptance
    def test_special_symbol_in_email(self, driver):
        specsym = AddContact(driver, Env.url)
        specsym.enter_data(first_name='Alíce', last_name="O'Green", email='alíce.s+mít@test.com',
                           phone='+1(650)7599755', street1='1101# Summit St', street2='244$ Aspen Hills Ct',
                           city='<Evanston>', state_province='&WY', country='{USA}')

        assert specsym.convert_to_line(first_name='Alíce', last_name="O'Green", email='alíce.s+mít@test.com',
                           phone='+1(650)7599755', street1='1101# Summit St', street2='244$ Aspen Hills Ct',
                           city='<Evanston>', state_province='&WY', country='{USA}') in specsym.return_contact_list()


    @pytest.mark.regression
    def test_emoji_in_email(self, driver):
        emoj = AddContact(driver, Env.url)
        emoj.enter_data(first_name='Alice😉', last_name="🍇Green",
                           street1='1101 Summit St😃', street2='244 Aspen Hills Ct😀',
                           city='🤯Evanston', state_province='🍉WY', country='USA👾')

        assert emoj.convert_to_line(first_name='Alice😉', last_name="🍇Green",
                           street1='1101 Summit St😃', street2='244 Aspen Hills Ct😀',
                           city='🤯Evanston', state_province='🍉WY', country='USA👾') in emoj.return_contact_list()
