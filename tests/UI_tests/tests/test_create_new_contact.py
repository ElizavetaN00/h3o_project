from tests.UI_tests.data_test.creds import AliceContactCreds
from tests.UI_tests.data_test.env import Env
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
