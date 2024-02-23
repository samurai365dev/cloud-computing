import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

if os.environ.get("RDS_HOSTNAME"):
    hostname = os.environ["RDS_HOSTNAME"]
    port = os.environ["RDS_PORT"]
    dbname = os.environ["RDS_DB_NAME"]
    username = os.environ["RDS_USERNAME"]
    password = os.environ["RDS_PASSWORD"]
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}/{dbname}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False}  # this is for sqlite
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
