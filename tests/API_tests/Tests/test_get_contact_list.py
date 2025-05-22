import pytest
import requests
from faker import Faker
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger, headers



@pytest.mark.get_contact_list
def test_get_contact_list(read_config, auth_token, registered_user, logger, headers):
    url = f"{read_config['URL']}/contacts"

    fake = Faker()
    def generate_contact():
        return {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            "email": fake.unique.email(),
            "phone": fake.msisdn()[:10],
            "street1": fake.street_address(),
            "street2": fake.secondary_address(),
            "city": fake.city(),
            "stateProvince": fake.state_abbr(),
            "postalCode": fake.postcode(),
            "country": fake.country()
        }

    # Creating 1st contact
    contact_1 = generate_contact()
    response_1 = requests.post(url, headers=headers, json=contact_1)
    assert response_1.status_code == 201, f"Error creating 1 contact: {response_1.status_code} {response_1.text}"

    # Creating 2nd contact
    contact_2 = generate_contact()
    response_2 = requests.post(url, headers=headers, json=contact_2)
    assert response_2.status_code == 201, f"Error creating 2 contact: {response_2.status_code} {response_2.text}"

    # Getting a list of contacts
    r_get = requests.get(url, headers=headers)
    assert r_get.status_code == 200, "Failed to get contact list"
    contacts = r_get.json()
    assert len(contacts) >= 2, "There must be at least two contacts in the list"

    logger.info(f"Contact list successfully received: {r_get.text}")
    logger.info(f"Status: {r_get.status_code}")
