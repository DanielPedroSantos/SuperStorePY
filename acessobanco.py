import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()  # lê as variáveis do .env

def acessobanco():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    port = int(os.getenv("DB_PORT"))
    dbname = os.getenv("DB_NAME")

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    )
    return engine