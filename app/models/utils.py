import psycopg2
from psycopg2 import sql

from sqlalchemy import create_engine, inspect

from app.models.data_models.client import ClientModel
from app.models.database.settings import config


def create_db():
    conn = None
    try:
        # 1. Устанавливаю  соединения с БД
        conn = psycopg2.connect(
            dbname="postgres",
            user=config.db_user,
            password=config.db_password,
            host=config.db_host,
            port=config.db_port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # 2. Проверка существования БД
        TARGET_DB = config.db_name
        cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [TARGET_DB])
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(TARGET_DB)))
            print(f"База '{TARGET_DB}' создана успешно")
        else:
            print(f"База '{TARGET_DB}' уже существует")

        cursor.close()

    except BaseException as e:
        print(f"Ошибка: {e}")

    finally:
        if conn:
            conn.close()


def init_db():
    database_url = f"postgresql://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
    engine = create_engine(database_url)
    inspector = inspect(engine)

    if not inspector.has_table(ClientModel.__tablename__):
        ClientModel.metadata.create_all(engine)
        print(f"Таблица '{ClientModel.__tablename__}' создана")
    else:
        print(f"Таблица '{ClientModel.__tablename__}' уже существует")
