"""
Responsible for executing buy/sell orders in response to a strategy signal.
"""
from abc import ABC, abstractmethod
from uuid import uuid4


class TradeOrder(ABC):
    """

    """

    def __init__(self):
        self.uid = uuid4()
        self.status = 'unknown'
        self.trade_type = 'unknown'

    @abstractmethod
    def execute(self):
        pass


class BuyOrder(TradeOrder):
    """

    """

    def __init__(self):
        super().__init__()
        self.trade_type = 'buy'
        self.buy_price = 0

    def execute(self):
        pass


class SellOrder(TradeOrder):
    """

    """

    def __init__(self):
        super().__init__()
        self.trade_type = 'sell'
        self.sell_price = 0

    def execute(self):
        pass


class TradeExecutor:
    """
    Responsible for executing buy/sell orders in response to a strategy or command signal.
    """

    def __init__(self):
        pass


if __name__ == '__main__':
    pass
