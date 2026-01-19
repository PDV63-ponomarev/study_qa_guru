from dataclasses import  dataclass
from enum import Enum

USER_ADULT_AGE = 18


class Status(Enum):
    students = 'student'
    worker = 'worker'


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE


    # dataclass выполняет эти функции

    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    # # функция для сравнения 2 классов
    # def __eq__(self, other):
    #     return (self.name == other.name and
    #             self.age == other.age and
    #             self.status == other.status and
    #             self.items == other.items)

class Worker(User):

    status = Status.worker

    def __init__(self, name, age ,items):
        self.name = name
        self.age = age
        self.items = items

    def do_work(self):
        pass

if __name__ == '__main__':

    d= {'name': 'Oleg',
        'age': 16,
        'status': 'students',
        'items': ['book','pen','paper']}

    oleg = User(name = 'Oleg', age = 16, status = Status.students, items = ['book','pen','paper'])
    oleg2 = User(name='Oleg', age=16, status=Status.students, items=['book', 'pen', 'paper'])
    olga = User(name='Olga', age=18, status=Status.worker, items=['book', 'paper'])

    # olga_worker = Worker(name='Olga', age=18, items=['book'])

    # у них разные id и они не равны
    # но изза __eq__ сравниваются значения
    assert  oleg == oleg2


    assert  oleg.age == 16
    assert  olga.age == 18

    olga.age += 1
    assert olga.age == 19


