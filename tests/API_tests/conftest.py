import json
import pytest
import os

# Путь к директории Test_Data (где лежат config.json, create_user_template.json и token.json)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "Test_Data"))


@pytest.fixture
def read_config():
    """
    Читает config.json из Test_Data
    """
    path = os.path.join(TEST_DATA_DIR, "config.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def read_cut():
    """
    Читает create_user_template.json из Test_Data
    """
    path = os.path.join(TEST_DATA_DIR, "create_user_template.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)
