import json
import pytest


@pytest.fixture
def read_config():
    with open ("../Test_Data/config.json") as f:
        data =  json.load(f)
    return data


@pytest.fixture
def read_cut():
    with open("../Test_Data/create_user_template.json") as f:
        data = json.load(f)
    return data


@pytest.fixture
def get_saved_token():
    with open("token.json", "r") as f:
        data = json.load(f)
    return data["token"]