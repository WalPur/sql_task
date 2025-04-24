# Проект

## Виртуальное окружение

Размещается по следующему пути `infra/apps/backend/.env`

```
DEBUG=1
SECRET_KEY="django-insecure-6*!9o=am-2p($@2abz4u2(w0q+j9a0dyqjfcf8_*kgp-cmz%ym"
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```

## Запуск контейнеров

Работы по докеру проводятся по следующему пути `infra/`

Установка и запуск контейнеров:

```
docker compose up --build -d
```

Применение миграций:

```
docker compose exec web python manage.py migrate --noinput
```

## Запуск команд

Для доступа к API имеется возможность использования графической оболочки
swagger по следующему адресу: `http://localhost:8000/api/schema/swagger`
