# 🚀 Запуск Certificate Service без Docker
## 1. Подготовка системы

Требования

    Python 3.10+

    PostgreSQL 14+

    Git

### Клонирование репозитория
git clone https://github.com/NadyaMamonova/Certificate_service.git

cd certificate_service

### Создание виртуального окружения
    python -m venv venv

### Активация окружения
#### Для Linux/MacOS:
    source venv/bin/activate

#### Для Windows:
    .\venv\Scripts\activate

## 2. Установка зависимостей 
    pip install -r requirements.txt

## 3. Настройка базы данных PostgreSQL

Создайте базу данных и пользователя:

    sudo -u postgres psql -c "CREATE DATABASE certificate_service;"
    sudo -u postgres psql -c "CREATE USER cert_user WITH PASSWORD 'yourpassword';"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE certificate_service TO cert_user;"

#### Настройте файл .env:

    DB_NAME=certificate_service
    DB_USER=cert_user
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=5432
    SECRET_KEY=django-insecure-your-secret-key-here


## 4. Применение миграций

    python manage.py migrate

## 5. Создание суперпользователя

    python manage.py createsuperuser

## 6. Запуск сервера

    python manage.py runserver

Сервер будет доступен по адресу: http://localhost:8000


## 7. Проверка работы

Откройте в браузере:

    API: http://localhost:8000/api/certificates/

    Админ-панель: http://localhost:8000/admin/

    Swagger UI: http://localhost:8000/swagger/


## 8. Запуск тестов

    python manage.py test certificates.tests