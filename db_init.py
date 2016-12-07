from db.schema import Messages
from db.db_url import db_url
from sqlalchemy import create_engine

url = db_url()
print('url:', url)
engine = create_engine(url)
Base.metadata.create_all(engine)
    
