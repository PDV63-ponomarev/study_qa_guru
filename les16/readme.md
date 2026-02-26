Управление зависимостями проекта
Что такое виртуальное окружение?
Что такое пакет?
Как Python управляет зависимостями?

Виртуальные окружения

pip - ставим пакеты
venv - виртуальное окружение из коробки
virtualenv - часть его стала venv. https://virtualenv.pypa.io/en/latest/index.html
pipenv - объединяем virtualenv и pip
https://github.com/pypa официальные инструменты для управления зависимостями
Poetry
https://python-poetry.org/
pyproject.toml https://peps.python.org/pep-0621/

Домашка
Создайте проект используя poetry. Заполните минимальную мета-информацию в pyproject.toml В зависимостях должны быть: pytest, selene В dev-зависимостях должен быть pylint

Дополнительно
https://github.com/pyenv/pyenv - управляем питонами
https://pip.pypa.io/en/stable/topics/secure-installs/ - как сделать pip более безопасным