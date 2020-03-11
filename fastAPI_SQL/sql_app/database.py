from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create database url for sqlalchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# create engine (check_same_thread is only for sqlite)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}        
)

# create sessionlocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create Base class
Base = declarative_base()


