from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:Shan1234$$@localhost:5432/shahanas"
engine = create_engine(db_url)
session = sessionmaker (autoflush = False, bind = engine)