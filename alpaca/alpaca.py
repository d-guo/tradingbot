import requests


class Alpaca:
    """Wrapper for Alpaca API
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


    def updateOrder(self, order_id, update_data):
        """Patch request to update parameters of an order

            Parameters:
                order_id: string id of the order to be updated
                update_data: dictionary with updated parameters as specified in the Alpaca API documentation
        
            Returns:
                dictionary with details of updated order
        """

        return requests.patch(f'{self.BASE_ENDPOINT}/v2/orders/{order_id}', json=update_data, headers=self.HEADER).json()


    def getOrder(self, order_id):
        """Get request to get order info of order with id order_id

            Parameters:
                order_id: string id of the order to be found
            
            Returns:
                dictionary with details of the order
        """

        return requests.get(f'{self.BASE_ENDPOINT}/v2/orders/{order_id}', headers=self.HEADER).json()


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

    
    def cancelOrder(self, order_id):
        """Delete request to cancel order with id order_id

            Parameters:
                order_id: string id of the order to be canceled
        """
        
        requests.delete(f'{self.BASE_ENDPOINT}/v2/orders/{order_id}', headers=self.HEADER)


    def cancelAllOrders(self):
        """Delete request to cancel all currently open orders

            Returns:
                list of objects with details on canceled orders
        """

        return requests.delete(f'{self.BASE_ENDPOINT}/v2/orders', headers=self.HEADER).json()


    def getPosition(self, symbol):
        """Get request to obtain details of position symbol

            Parameters:
                symbol: string of position symbol
            
            Returns:
                dictionary with details of position
        """

        return requests.get(f'{self.BASE_ENDPOINT}/v2/positions/{symbol}', headers=self.HEADER).json()


    def getOpenPositions(self):
        """Get request to obtain list of open positions

            Returns:
                list of position dictionaries with details of open positions
        """

        return requests.get(f'{self.BASE_ENDPOINT}/v2/positions', headers=self.HEADER).json()
    

    def closePosition(self, symbol):
        """Delete request to close position symbol

            Parameters:
                symbol: string of position symbol
            
            Returns:
                dictionary with details of the order
        """

        return requests.delete(f'{self.BASE_ENDPOINT}/v2/positions/{symbol}', headers=self.HEADER).json()

    
    def closeAllPositions(self):
        """Delete request to close all position
            
            Returns:
                list of objects with details on closed positions
        """

        return requests.delete(f'{self.BASE_ENDPOINT}/v2/positions', headers=self.HEADER).json()


    def getAsset(self, symbol):
        """Get request to obtain details of asset symbol

            Parameters:
                symbol: string of asset symbol
            
            Returns:
                dictionary with details of asset
        """

        return requests.get(f'{self.BASE_ENDPOINT}/v2/assets/{symbol}', headers=self.HEADER).json()


    def getAllAssets(self):
        """Get request to obtain list of all assets (both active and inactive)

            Returns:
                list of dictionaries with details of all assets
        """

        return requests.get(f'{self.BASE_ENDPOINT}/v2/assets', headers=self.HEADER).json()
    

    def getClock(self):
        """Get request to obtain time from Alpaca API

            Returns:
                dictionary with clock information
        """

        return requests.get(f'{self.BASE_ENDPOINT}/v2/clock', headers=self.HEADER).json()