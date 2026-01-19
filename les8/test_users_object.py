import csv
import pytest

from les8.models.users import User, USER_ADULT_AGE, Status, Worker
from les8.provaiders import UserProvider, CsvUserProvider


# исп обьектный подход работы с данными

@pytest.fixture
def user_provider() -> UserProvider:
    return CsvUserProvider()


@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture
def workers(users) -> list[Worker]:
    # берем только работников из списка пользователей
    workers = [Worker(name=user.name, age=user.age, items=user.items)
               for user in users if user.status == Status.worker]
    return workers


# def user_is_adult(user: User):
#     return user.age >= USER_ADULT_AGE


def test_workers_are_adul2(workers):
    # тестируем что все работники старше 18
    for worker in workers:
        # assert User.age >= USER_ADULT_AGE, f'User {worker.name} little {USER_ADULT_AGE}'
        assert worker.is_adult(), f'User {worker.name} young {USER_ADULT_AGE}'
        # assert not worker.is_adult(), f'User {worker.name} older {USER_ADULT_AGE}'
