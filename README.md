# Team: 
h3o 

# Project Title
Test framework for automated testing of the [Contact List App](https://thinking-tester-contact-list.herokuapp.com/) project

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
