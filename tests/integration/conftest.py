import pytest


@pytest.fixture
def first_client_dict():
    return {
        'first_name': "Иван",
        'last_name': "Иванов",
        'middle_name': "Иванович",
        'email': "ivanov@mail.ru",
        'phone_number': "+79876543210",
        'password': "qwerty"
    }
