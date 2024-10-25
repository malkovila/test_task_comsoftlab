# Email Integration Project

Этот проект на Django реализует интеграцию сообщений из почтовых сервисов, таких как Yandex, Gmail и Mail.ru, и использует `Django Channels` для асинхронного чтения почты и прогресс-бара. Проект упакован в Docker и включает PostgreSQL в качестве базы данных и Redis для `Channels`.

## Установка и запуск

### Предварительные требования

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Шаги установки

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/malkovila/test_task_comsoftlab.git
    cd email_integration
    ```

2. Создайте файл `requirements.txt` с зависимостями:

    ```plaintext
    Django==4.2
    djangorestframework==3.14.0
    channels==4.0.0
    channels-redis==4.1.0
    daphne==4.0.0
    psycopg2-binary==2.9.3
    ```

3. Соберите и запустите контейнеры с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

4. Выполните миграции базы данных, создайте суперпользователя и соберите статику (выполняется в другом терминале, когда контейнеры уже запущены):

    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    docker-compose exec web python manage.py collectstatic --noinput
    ```

### Доступ к проекту

После запуска приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

### Описание

- **PostgreSQL** используется для хранения информации о пользователях и сообщениях.
- **Redis** работает как бэкенд каналов для обработки WebSocket-соединений.
- **Daphne** обрабатывает асинхронные запросы для обеспечения работы WebSocket.

### Основные компоненты

- **Модели**:
  - `EmailAccount`: хранит логины и пароли.
  - `EmailMessage`: хранит данные сообщений, включая текст и вложения.
- **WebSocket**: обеспечивает прогресс-бар на фронтенде для отображения состояния импорта.
- **API**: реализован с использованием `Django REST Framework` для доступа к сообщениям.

### Полезные команды

- Остановка контейнеров:

    ```bash
    docker-compose down
    ```

- Повторная сборка контейнеров:

    ```bash
    docker-compose up --build
    ```

## Авторизация в админке

Используйте данные суперпользователя, созданные ранее, для доступа к админке по адресу [http://localhost:8000/admin](http://localhost:8000/admin).

### Заметки

- В Docker-среде переменные окружения для базы данных и Redis берутся из `docker-compose.yml`.
- Проект настроен на работу с PostgreSQL и Redis в контейнерах, не требует локальных установок для этих компонентов.

---

Проект `Email Integration` полностью настроен для работы в Docker-среде с минимальной конфигурацией и готов к использованию для обработки сообщений из почтовых сервисов.
