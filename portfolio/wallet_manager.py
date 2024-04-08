class WalletManager:
    def __init__(self):
        self._wallets_enabled = []
        self._wallets_available = []

    @property
    def enabled_wallets(self):
        return self._wallets_enabled

    @property
    def wallets(self):
        return self._wallets_available + self._wallets_enabled
