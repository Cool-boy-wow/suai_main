Описание: Этот проект представляет собой бэкенд, который взаимодействует с GitLab репозиторием пользователя. Он поддерживает основные события в репозитории на ветку master: commit, push, merge.

Требования: Python 3.6+ FastAPI Uvicorn python-gitlab sqlite3

Установка: Клонируйте репозиторий: git clone https://gitlab.com/cool-boy-wow/suai.git

Запустите сервер: uvicorn main:app --reload

Использование: Бэкенд будет логировать все события push и merge в файл events.log. Каждое событие будет обработано, информация о нем будет записана в базу данных SQLite.

Тестирование: Чтобы протестировать бэкенд, вы можете создать push или merge request в вашем репозитории. В лог файле должны появиться соответствующие записи.

Контакты: Если у вас возникли проблемы или вопросы, пожалуйста, свяжитесь с нами по адресу anvar.rakhmonoff@yandex.ru

user-email: cool.boy.wow@yandex.ru
access-token: glpat-ax-mynrFQGquZ4hMopz1