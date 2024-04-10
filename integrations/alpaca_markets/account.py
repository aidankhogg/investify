from integrations.alpaca_markets.api import alpaca_client
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.requests import GetAssetsRequest
import humanfriendly
trading_client = alpaca_client

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(humanfriendly.format_number(account.buying_power)))

# Get our account information.
account = trading_client.get_account()

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')
