# Certificate Service API
### Сервис генерации и управления цифровыми сертификатами

## 🔍 Описание сервиса

Certificate Service – это RESTful API для создания, хранения и управления цифровыми сертификатами о прохождении стажировок. Сервис предоставляет:

✅ Гибкую систему учета сертификатов

✅ Интеграцию с образовательными учреждениями

✅ Автоматическую генерацию сертификатов

✅ Безопасный доступ через JWT-аутентификацию

⚙️ Основные возможности
1. Управление сертификатами

    📄 Создание/просмотр сертификатов

    🔍 Поиск по email пользователя

    🏷️ Фильтрация по навыкам и ролям

    📅 Автоматическое проставление дат выдачи

2. Интеграция с образовательными системами

    🏫 Привязка к учебным заведениям (Schools)

    🛠️ Учет приобретенных навыков (Skills)

    👨‍💻 Указание ролей (Roles)

3. Безопасность и доступ

    🔐 JWT-аутентификация

    👮‍♂️ Разграничение прав доступа

    📊 Админ-панель Django

4. Документирование API

    📚 Swagger UI – интерактивная документация

    📖 ReDoc – альтернативное представление API



🛠 Технологический стек

    Backend - Django 4.2 + DRF 3.14
    База данных	- PostgreSQL 16
    Аутентификация	- JWT
    Документация	- Swagger UI + ReDoc