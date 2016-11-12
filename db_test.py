from db.schema import Messages
from db.db_url import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = db_url()
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

m1 = Messages(msg_id = 2,
              msg_type = 'trollboxMessage',
              username = 'elSamu',
              msg_text = 'This is the first msg (hopefully)',
              user_rep = 1000)

m2 = Messages(msg_id = 13,
              msg_type = 'trollboxMessage',
              username = 'notElSamu',
              msg_text = 'number #2',
              user_rep = 1)
session.bulk_save_objects([m1, m2])
session.commit()
