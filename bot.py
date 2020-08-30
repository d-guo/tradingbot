import requests

class TradingBot:
    """Class to performs trades using Alpaca API

    Uses:
        1. wrapper for Alpaca API
        2. implement strategy and deploy to some cloud service
    """

    def __init__(self, path_to_config):
        """Initializes class with keys from config file located at path_to_config

            Parameters:
                path_to_config: string of path to config file which has ID and SECRET keys
        """

        self.BASE_ENDPOINT = 'https://paper-api.alpaca.markets'  # configure as https://api.alpaca.markets for live trading

        with open(path_to_config) as f:
            self.ID_KEY, self.SECRET_KEY = f.read().splitlines()
        
        self.HEADER = {
            'APCA-API-KEY-ID': self.ID_KEY,
            'APCA-API-SECRET-KEY': self.SECRET_KEY
        }
        self.account_info = self._getAccountInfo()

    def _getAccountInfo(self):
        """Get request to obtain account info associated with ID and SECRET keys

            Returns:
                dictionary with account info
        """

        return requests.get(f'{self.BASE_ENDPOINT}/v2/account', headers=self.HEADER).json()

    def createOrder(self, order_data):
        """Post request to place order described by order_data
        
            Parameters:
                order_data: dictionary with order details as specified in the Alpaca API documentation
            
            Returns:
                dictionary with details of the new order
        """

        return requests.post(f'{self.BASE_ENDPOINT}/v2/orders', json=order_data, headers=self.HEADER).json()

    def cancelOrder(self, order_id):
        """Delete request to cancel order with id order_id

            Parameters:
                order_id: string id of the order to be canceled
        """
        
        requests.delete(f'{self.BASE_ENDPOINT}/v2/orders/{order_id}', headers=self.HEADER)

    def getOpenOrders(self):
        """Get request to obtain list of open orders

            Returns:
                list of all order dictionaries for open orders in order of most recent to oldest
                    - order dictionary contains details of an order
        """

        # define request params to only list up to 100 open orders during any time of day in descending chronological order (recent to oldest)
        params = {
            'status': 'open',
            'limit': 100,
            'after': -1,
            'until': 2400,
            'direction': 'desc',
            'nested': True
        }

        return requests.get(f'{self.BASE_ENDPOINT}/v2/orders', json=params, headers=self.HEADER).json()

# testing
# places an order for apple stock and immediately cancels it

tb = TradingBot('keys.cfg')

order_data = {
    'symbol': 'AAPL',
    'qty': 1,
    'side': 'buy',
    'type': 'market',
    'time_in_force': 'day',
    'limit_price': None,
    'stop_price': None,
    'extended_hours': False,
    'client_order_id': None
}

tb.createOrder(order_data)
open_orders = tb.getOpenOrders()
print(open_orders)
tb.cancelOrder(open_orders[0]['id'])
print(tb.getOpenOrders())