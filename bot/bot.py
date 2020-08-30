from alpaca.alpaca import Alpaca


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
        """Invokes bot's decision making after updating and places orders accordingly.
        """

        pass