from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner

from db.schema import Messages, Tickers
from db.db_url import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from asyncio import coroutine

VALID_PAIRS = ['BTC_ETH', 'USDT_ETH', 'USDT_BTC']

class PoloniexComponent(ApplicationSession):
    def onConnect(self):
        print('Starting database connection')
        url = db_url()
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        print('Database connection successful')

        self.ticker_buffer = []
        self.msg_buffer = []
        self.join(self.config.realm)
        
        
    @coroutine
    def onJoin(self, details):

        def onMessage(*args):
            # Stores messages when they're received by the ticker
            try:
                msg = Messages(msg_id = args[1],
                               msg_type = args[0][:50],
                               username = args[2][:50],
                               msg_text = args[3][:500],
                               user_rep = args[4])
                self.msg_buffer.append(msg)
            except IndexError:
                print('The msg length was not long enough')

            if len(self.msg_buffer) > 10:
                self.session.bulk_save_objects(self.msg_buffer)
                self.session.commit()
                self.msg_buffer = []

            print(self.msg_buffer)
            print(len(self.msg_buffer))


        def onTicker(*args):
            # Stores ticker events when received by ticker
            currency_pair = args[0]

            if currency_pair in VALID_PAIRS:
                print('Current pair: ', currency_pair)
                ticker = Tickers(currency_pair = args[0],
                                 last = args[1],
                                 lowest_ask = args[2],
                                 highest_bid = args[3],
                                 percent_change = args[4],
                                 base_volume = args[5],
                                 quote_volume = args[6],
                                 is_frozen = bool(args[7]),
                                 day_high = args[8],
                                 day_low = args[9])
                self.ticker_buffer.append(ticker)

            if len(self.ticker_buffer) > 10:
                # Dump buffer contents to database
                self.session.bulk_save_objects(self.ticker_buffer)
                self.session.commit()
                self.ticker_buffer = []
                    
        try:
            yield from self.subscribe(onMessage, 'trollbox')
        except Exception as e:
            print("Could not subscribe to topic:", e)

        try:
            yield from self.subscribe(onTicker, 'ticker')
        except Exception as e:
            print("Could not subscribe to topic:", e)
            

def main():
    runner = ApplicationRunner("wss://api.poloniex.com:443", "realm1")
    runner.run(PoloniexComponent)


if __name__ == "__main__":
    main()
