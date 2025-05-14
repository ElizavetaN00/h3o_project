"""
Data классы, реализованные с помощью декоратора @dataclass предназначены для создания классов,
основное назначение которых — хранение данных (такие классы предназначены для хранения некоторого
состояния, некоторых данных и когда не требуется какое-то поведение в виде функций.).
"""
import dataclasses


@dataclasses.dataclass
class Env:
    """
    Класс для хранения конфигурационных данных тестового окружения.
    Атрибуты класса:
        url: Базовый URL тестового приложения
        documenter: Ссылка на документацию API в Postman
        contact_list: Эндпоинт для работы со списком контактов
    """
    url = "https://thinking-tester-contact-list.herokuapp.com/"
    documenter = "https://documenter.getpostman.com/view/4012288/TzK2bEa8"
    contact_list = "https://thinking-tester-contact-list.herokuapp.com/contactList"
    addUser_url = "https://thinking-tester-contact-list.herokuapp.com/addUser"
