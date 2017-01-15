from datetime import datetime
from sqlalchemy import Table, Column, Numeric, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db.db_url import db_url
from sqlalchemy import create_engine

Base = declarative_base()

class Messages(Base):

    __tablename__ = 'messages'

    msg_id = Column(Integer(), primary_key=True)
    msg_type = Column(String(50))
    username = Column(String(50))
    msg_text = Column(String(500))
    user_rep = Column(Integer())
    msg_time = Column(DateTime(), default=datetime.now)


def initialise_messages_table():
    url = db_url()
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    print('Iinitialised the Messages table')

    
if __name__=="__main__":
    initialise_messages_table()
