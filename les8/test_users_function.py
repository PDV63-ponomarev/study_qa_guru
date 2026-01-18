import csv
import pytest

# исп функциональный подход
# выносим логику в отд функции и фикстуры

@pytest.fixture
def users():
    # открывает файл
    with open('users.csv') as f:
        users = list(csv.DictReader(f, delimiter=';'))
    return users


@pytest.fixture
def workers(users):
    # берем только работников из списка пользователей
    workers = [user for user in users if user['status'] == 'worker']
    return workers


def user_is_adult(user):
    return int(user['age']) >= 18


def test_workers_are_adul2(workers):
    # тестируем что все работники старше 18
    for worker in workers:
        assert user_is_adult(worker), f'User {worker['name']} little 18'


