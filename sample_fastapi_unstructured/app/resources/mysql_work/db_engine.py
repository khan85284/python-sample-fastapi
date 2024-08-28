from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL_DATABASE = "mysql+pymysql://root:test1234!@localhost:3306/"

engine = create_engine("sqlite:///db.sqlite3", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
