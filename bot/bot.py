import logging

from ..alpaca.alpaca import Alpaca


class TradingBot:
    """Trading bot uses the Alpaca API to place orders

        Usage:
            after setup, call invoke method periodically to activate bot's decision making
            bot will decide whether or not to place orders and what orders to place
    """

    def __init__(self):
        """Set up Alpaca API to use for placing orders
        """

        self.alpaca = Alpaca('keys.cfg')
    

    def _update(self):
        """Updates bot's knowledge of market trends
        """

        pass


    def invoke(self):
        """Invokes bot's decision making after updating and places orders accordingly

            Current Usage: just buys and sells 2 AAPL shares every day
        """

        START_b, END_b, START_s, END_s = '00:00', '00:05', '12:00', '12:05'
        current_time = self.alpaca.getClock()['timestamp'][11:16]
        logging.info(f'alpaca time: {current_time}')
        
        aapl_order = {
            'symbol': 'AAPL',
            'qty': 2,
            'type': 'market',
            'time_in_force': 'day',
            'limit_price': None,
            'stop_price': None,
            'extended_hours': False,
            'client_order_id': None
        }

        if START_b <= current_time < END_b:
            aapl_order['side'] = 'buy'
            self.alpaca.createOrder(aapl_order)
            logging.info('bought 2 aapl stock')

        elif START_s <= current_time < END_s:
            if len(self.alpaca.getOpenOrders()) != 0:
                self.alpaca.cancelAllOrders()
                logging.info('canceled open order for aapl stock')
            elif int(self.alpaca.getPosition('AAPL')['qty']) != 0:
                aapl_order['side'] = 'sell'
                self.alpaca.createOrder(aapl_order)
                logging.info('sold 2 aapl stock')
            else:
                logging.info('did nothing... no expected profit')

        else:
            logging.info('did nothing... not within optimal hours')