# Team: 
h3o 

# Project Title
A Python-based automation testing framework for the **Contact List App**, covering both UI and API testing. The project follows the Page Object Model (POM) pattern and incorporates best practices in automated testing.

# Project structure
```
...
├── h3o_project/
│   ├── github/
│   ├── workflows/
│   ├── mypy.yaml
│   └── pylint.yaml
├── tests/
│   ├── API_tests/
│   │   ├── Test_Data/
│   │   │   └── config.json
│   │   ├── Tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_add_contact.py
│   │   │   ├── test_add_user.py
│   │   │   ├── test_delete_contact.py
│   │   │   ├── test_delete_user.py
│   │   │   ├── test_get_contact.py
│   │   │   ├── test_get_contact_list.py
│   │   │   ├── test_get_user_profile.py
│   │   │   ├── test_update_contact(patch).py
│   │   │   ├── test_update_contact(put).py
│   │   │   ├── test_update_user_info.py
│   │   │   ├── test_user_log_In.py
│   │   │   └── test_user_log_out.py
│   │   └── conftest.py
│   ├── UI_tests/
│   │   ├── data_test/
│   │   │   ├── __init__.py
│   │   │   ├── constants.py
│   │   │   ├── creds.py
│   │   │   ├── env.py
│   │   │   └── locators.py
│   │   ├── pages/
│   │   │   ├── __init__.py
│   │   │   ├── add_contact.py
│   │   │   ├── add_user_page.py
│   │   │   ├── base_page.py
│   │   │   └── contact_details.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_contact_details.py
│   │   │   ├── test_create_new_contact.py
│   │   │   ├── test_navigation.py
│   │   │   ├── test_user_log.py
│   │   │   └── test_user_registration.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   └── __init__.py
├── .gitignore 
├── app.py
├── Dockerfile
├── Jenkinsfile_api
├── Jenkinsfile_ui
├── LICENSE 
├── README.md
└── requirements.txt
```

# Technologies Used
- Python
- PyTest
- Selenium
- Requests
- Logging
- Faker
- PyTest Fixtures
- OOP (Object-Oriented Programming)
- Allure Reports
- Docker
- Jenkins
- GitHub
- Postman
- Kaiten

# How to install
Clone this repository:

```bash
git clone https://github.com/ElizavetaN00/h3o_project.git

Create a virtual environment and activate it:
pip install virtualenv
cd ~/projects/pytest-framework
virtualenv venv
source venv/bin/activate     # for Linux/macOS
venv\Scripts\activate.bat    # for Windows

Install dependencies:
pip install -r requirements.txt

# How to run

To execute ALL tests:
pytest .

To execute UI tests:
cd .\tests\UI_tests\          # for Windows
cd ./tests/UI_tests/          # for Linux/macOS
pytest .

To execute API tests:
cd .\tests\API_tests\         # for Windows
cd ./tests/API_tests/         # for Linux/macOS
pytest .

To execute marks in UI tests:
cd .\tests\UI_tests\          # for Windows
cd ./tests/UI_tests/          # for Linux/macOS
pytest .
pytest -m "mark"
