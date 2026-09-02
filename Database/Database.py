# import psycopg2 
# from dotenv import load_dotenv
# import os
# from sqlalchemy import DeclarativeBase

# load_dotenv()

# class Database:
#     def __init__(self):
#         self.host = os.getenv("host")
#         self.port = os.getenv("port")
#         self.database = os.getenv("database")
#         self.user = os.getenv("user")
#         self.password = os.getenv("password")
#         self.connection = None

#     def connect(self):
#         self.connection = psycopg2.connect(
#             host = self.host,
#             port = self.port,
#             database = self.database,
#             user = self.user,
#             password = self.password
#         )
#         if not self.connection:
#             print("conectado com sucesso")
#             return self.connection
#         if self.connection:
#             print("ja esta conectado")
#             pass

#     def close_connect(self):
#         if self.connection:
#             self.connection.close()
#             print("Desconectado com sucesso")

#     def execute_query(self ,paramer: dict[str, str]):
#         cursor = self.connection.cursor()
#         cursor.execute(paramer)
#         resultado = cursor.fetchall()
#         return resultado


############################################## VERSAO SQLALCHEMY ####################################################
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('user')}:"
    f"{os.getenv('password')}@"
    f"{os.getenv('host')}:"
    f"{os.getenv('port')}/"
    f"{os.getenv('database')}"
)


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass