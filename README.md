# Тестовое задание для Placebo/25

## Установка и запуск

### С использованием Docker

1. Убедитесь, что у вас установлен Docker.
2. Склонируйте репозиторий:

    ```bash
    $ git clone https://github.com/saltitc/employees_api.git
    $ cd employees_api
    ```

3. Соберите и запустите Docker-контейнер:

    ```bash
    $ docker-compose build
    $ docker-compose up
    ```

4. Откройте браузер и перейдите по адресу `http://localhost:8000/redoc/`.
---
> Остановить контейнеры:
>
>    ```bash
>    $ docker-compose down
>    ```
---
### Без использования Docker

1. Создайте виртуальное окружение и активируйте его:

    ```bash
    $ python -m venv venv
    $ source venv/bin/activate  # Для Unix
    $ .\venv\Scripts\activate  # Для Windows
    ```

2. Установите зависимости:

    ```bash
    $ pip install -r requirements.txt
    $ cd company_structure/
    ```

3. Примените миграции:

    ```bash
    $ python manage.py migrate
    ```
4. Загрузите фикстуры:

    ```bash
    $ python manage.py loaddata employees/fixtures/*.json
    ```
   
5. Запустите сервер разработки:

    ```bash
    $ python manage.py runserver
    ```

6. Откройте браузер и перейдите по адресу `http://localhost:8000/redoc/'.

---
>Деактивировать виртуальное окружение:
>
>    ```bash
>    $ deactivate
>    ```
---