import csv

# прямолинейный вариант теста

def test_workers_are_adult():

    # тестируем что все работники старше 18

    with open('users.csv') as f:
        users = csv.DictReader(f, delimiter=';')
        workers = [user for user in users if user['status'] == 'worker']

    for worker in workers:
        assert int(worker['age']) >= 18, f'User {worker['name']} little 18'


        # {key: value for key, value in some_dict.items() if...}

        # workers = []
        # for user in users:
        #     if user['status'] == 'worker':
        #         workers.append(user)

