from agent.markets.trading import Markets, Assets, Fees


class Cryptocurrency(Assets):
    def __init__(self):
        super().__init__()


class CurrencyPair(Assets):
    def __init__(self):
        super().__init__()
        self._a = Cryptocurrency()
        self._b = Cryptocurrency()
