from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class RSADb:
    NAME = ''
    USER = 'root'
    HOST = ''
    PORT = 0
    PASSWORD = ''

    SQLALCHEMY_URL = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'

    ENGINE = create_engine(SQLALCHEMY_URL)

    Session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )

    @staticmethod
    def get_db() -> Session:
        db = RSADb.Session()
        try:
            yield db
        finally:
            db.close()


Base = declarative_base()
