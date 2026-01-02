from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Float, String, Column 

Base = declarative_base()

class Notes (Base):

    __tablename__ = "Notes"
    note_id = Column (Integer, primary_key = True, index = True)
    note_name = Column (String)
    note_content = Column (String)