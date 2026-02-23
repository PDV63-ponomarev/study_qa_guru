Хуки pytest: https://docs.pytest.org/en/7.3.x/reference/reference.html#hooks

Примерное дерево хуков - pytest-dev/pytest#3261 (comment)
pytest_addoption - добавляем новые опции
pytest_configure - меняем что-нибудь в конфигурации
pytest_sessionstart - делаем что-нибудь перед стартом всех тестов
pytest_generate_tests - изменяем параметризацию тестов
pytest_collection_modifyitems - редактируем собранные тесты
pytest_runtestloop - хуки во время выполнения тестов
pytest_sessionfinish - все тесты завершились
xdist

хуки - это спец функции выполн в разные моменты жизн цикла pytest
 

xdist
позволяет одновременно запустить несколько тестов
pytest -k test_sleep -v -n 4
pytest -k test_sleep -v -n auto
-n аргумент
фикстуры xdist
как себя ведут session scope фикстуры?
Как заставить session scope фикстуру выполниться один раз 
https://pytest-xdist.readthedocs.io/en/latest/how-to.html

