# Тестовое задание для Placebo/25

## Установка и запуск

### С использованием Docker

1. Убедитесь, что у вас установлен Docker.
2. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/saltitc/employees_api.git
    cd employees_api
    ```

3. Соберите и запустите Docker-контейнер:

    ```bash
    docker-compose build
    docker-compose up
    ```

4. Откройте браузер и перейдите по адресу `http://localhost:8000`.
---
- Остановить контейнеры:

    ```bash
    docker-compose down
    ```
---
### Без использования Docker

1. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Unix
    .\venv\Scripts\activate  # Для Windows
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    cd company_structure/
    ```

3. Примените миграции:

    ```bash
    python manage.py migrate
    ```
4. Загрузите фикстуры:

    ```bash
    python manage.py loaddata employees/fixtures/*.json
    ```
   
5. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

6. Откройте браузер и перейдите по адресу `http://localhost:8000`.

---
- Деактивировать виртуальное окружение:

    ```bash
    deactivate
    ```
---
## Документация к API

API предоставляет следующие эндпоинты:

###  `/api/departments/`

- **Методы:**
  - `GET`: Получение списка всех отделов в организации.
  - `POST`: Создание нового отдела.

- **Примеры запросов:**
  - Получение списка отделов:
    ```bash
    curl http://localhost:8000/api/departments/
    ```
  - Создание нового отдела:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "New Department"}' http://localhost:8000/api/departments/
    ```

---

### `/api/positions/`

- **Методы:**
  - `GET`: Получение списка всех должностей в организации.
  - `POST`: Создание новой должности.

- **Примеры запросов:**
  - Получение списка должностей:
    ```bash
    curl http://localhost:8000/api/positions/
    ```
  - Создание новой должности:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "New Position"}' http://localhost:8000/api/positions/
    ```

---

### `/api/employees/`

- **Методы:**
  - `GET`: Получение списка всех сотрудников в организации.
  - `POST`: Создание нового сотрудника.

- **Примеры запросов:**
  - Получение списка сотрудников:
    ```bash
    curl http://localhost:8000/api/employees/
    ```
  - Создание нового сотрудника:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "department": 1}' http://localhost:8000/api/employees/
    ```

---

### `/api/permissions/`

- **Методы:**
  - `GET`: Получение списка всех прав сотрудников в организации.
  - `POST`: Создание нового права сотрудника.

- **Примеры запросов:**
  - Получение списка прав сотрудников:
    ```bash
    curl http://localhost:8000/api/permissions/
    ```
  - Создание нового права сотрудника:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"position": 1, "name": "Code Access"}' http://localhost:8000/api/permissions/
    ```

---