# Electronics Network API

## Описание
Данное веб-приложение представляет собой API-интерфейс и админ-панель для управления сетью по продаже электроники. Приложение построено на Django и Django REST Framework (DRF), поддерживает иерархическую структуру сети и фильтрацию данных.

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/nikita-szr/Electronics_sell_network/tree/feature_1
cd electronics_network
```

### 2. Установка зависимостей
Создайте и активируйте виртуальное окружение, затем установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Применение миграций и создание суперпользователя
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Запуск сервера
```bash
python manage.py runserver
```

## Использование API

### Доступные эндпоинты
- `/api/network_nodes/` — CRUD-операции для узлов сети
- `/api/products/` — CRUD-операции для продуктов

### Примеры запросов
#### Получение списка узлов сети
```bash
GET /api/network_nodes/
```
#### Фильтрация узлов сети по стране
```bash
GET /api/network_nodes/?country=Россия
```

## Админ-панель
Админ-панель доступна по адресу:
```bash
http://127.0.0.1:8000/admin/
```

## Права доступа
Только активные сотрудники могут работать с API. Для аутентификации используйте `/api-auth/login/`.

## Дополнительные функции
- Фильтр по названию города в админке
- Очистка задолженности через `admin action`

## Зависимости
- requirements.txt

## Запуск через docker
- docker-compose up --build

