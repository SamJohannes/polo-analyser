from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner

from db.schema import Messages
from db.db_url import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from asyncio import coroutine
import nltk


coins = [['btc', 'bitcoin'], ['fct', 'factom'], ['eth', 'ether', 'ethereum'],
         ['xrp', 'ripple'], ['ltc', 'litecoin'], ['xmr', 'monero'],
         ['etc'], ['dash'], ['steem'], ['nem'], ['maid', 'maidsafecoin'], ['lsk', 'lisk']]

class PoloniexComponent(ApplicationSession):
    def onConnect(self):
        print('at the start of the log')
        url = db_url()
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
        self.join(self.config.realm)
        
    @coroutine
    def onJoin(self, details):
        def onTicker(*args):
            try:
                msg = Messages(msg_id = args[1],
                               msg_type = args[0][:50],
                               username = args[2][:50],
                               msg_text = args[3][:500],
                               user_rep = args[4])
            except IndexError:
                print('The msg length was not long enough')

            print(msg)
            
            
        try:
            yield from self.subscribe(onTicker, 'trollbox')
        except Exception as e:
            print("Could not subscribe to topic:", e)

    def getScore(self, msg):
        pass

    def updateScore(self, score, currency):
        pass

    def initialiseScores(self):
        self.scores = {}
        for coin in coins:
            self.scores[coin] = 0
        print('scores')


def main():
    runner = ApplicationRunner("wss://api.poloniex.com:443", "realm1")
    runner.run(PoloniexComponent)


if __name__ == "__main__":
    main()
