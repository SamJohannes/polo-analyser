from datetime import datetime
from sqlalchemy import Table, Column, Numeric, Boolean, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db.db_url import db_url
from sqlalchemy import create_engine

Base = declarative_base()

DECIMAL_PLACES = 8
SIG_FIGS = 16

class Tickers(Base):

    __tablename__ = 'tickers'

    currency_pair = Column(String(10), primary_key=True)
    last = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))
    lowest_ask = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))
    highest_bid = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))    
    percent_change = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))    
    base_volume = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))    
    quote_volume = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))    
    is_frozen = Column(Boolean())
    day_high = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))    
    day_low = Column(Numeric(SIG_FIGS, DECIMAL_PLACES))    
    msg_time = Column(DateTime(), default=datetime.now, primary_key=True)


def initialise_tickers_table():
    url = db_url()
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    print('Initialised the Tickers table')

    
if __name__=="__main__":
    initialise_tickers_table()
