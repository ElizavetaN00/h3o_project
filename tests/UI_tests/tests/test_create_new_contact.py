from tests.UI_tests.data_test.creds import AliceContactCreds
from tests.UI_tests.data_test.env import Env
from tests.UI_tests.pages.addContact import AddContact


def test_all_fields(driver):

    afs = AddContact(driver, Env.url)
    afs.enter_data(*AliceContactCreds.return_contact_info)

    assert afs.convert_to_line(*AliceContactCreds.return_contact_info) in afs.return_contact_list()
