from alpaca.data import StockHistoricalDataClient
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.historical.option import OptionHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from integrations.alpaca_markets.api import connection_details
# No keys required for crypto data
crypto_client = CryptoHistoricalDataClient()

# Creating request object
request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD"],
    timeframe=TimeFrame.Day,
    start="2022-09-01",
    end="2022-09-07"
)

# Retrieve daily bars for Bitcoin in a DataFrame and printing it
btc_bars = crypto_client.get_crypto_bars(request_params)

# Convert to dataframe
print(btc_bars.df)

stock_client = StockHistoricalDataClient(connection_details.key,  connection_details.secret)
option_client = OptionHistoricalDataClient(connection_details.key,  connection_details.secret)
