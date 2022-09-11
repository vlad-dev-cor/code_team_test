### Инструкция по запуску сервиса

**Настройка среды**
Переименовать sample.env в .env
```bash
sudo cp sample.env .env
```

**Создать сеть внутри docker**

```bash
docker network create -d bridge local-apps
```

**Настроить и запустить БД PostgreSQL**

1. ```bash
   sudo docker run --name local-pg14 \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_INITDB_ARGS="--locale=C.UTF-8" \
    -v ~/Documents/storedata/pg-data14:/var/lib/postgresql/data \
    -p 5443:5432 \
    --network="local-apps" \
    --restart always \
    -d postgres:14-alpine
   ```

2. ```bash
    sudo docker exec -it local-pg14 psql -U postgres
    ```

    ```bash
    CREATE USER dish CREATEDB LOGIN PASSWORD 'dish';
    CREATE DATABASE dish WITH OWNER = dish CONNECTION LIMIT = -1;
    GRANT ALL PRIVILEGES ON DATABASE dish to dish;
    ```

3. Выйти из SQL promt `\q`

**Запустить django сервер**

1. Скопировать репозиторий
2. ```bash
   docker build -t dish/python38_django_4:base -f DockerfileControlPanelBase . --no-cache
   ```
3. ```bash
   docker build -t dish/dish-server:base -f DockerfileControlPanel . --no-cache
   ```
4. Команда запуска
   ```bash
   docker-compose -f docker-compose.yml up
   ```
5. в терминале зайти в контейнер
   ```bash
   docker exec -it django_test_dishweb_1 bash
   ```
6. Сделать миграцию
   ```bash
   python3.8 manage.py migrate
   ```
7. Создаем админа
   ```bash
   python3.8 manage.py createsuperuser
   ```

**Работа с проектом**

1. В админке создаем категории и продукты
   http://0.0.0.0:8003/admin/
2. В сваггере можно протестировать запрос в базу
   http://0.0.0.0:8003/swagger/

**Тестирование прокта**

   ```bash
   docker-compose -f docker-compose-test.yml up
   ```