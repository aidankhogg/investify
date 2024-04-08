import os.path

from alpaca.trading.client import TradingClient
from engine.configured import load_single_conf_file, local_paths

connection_details = load_single_conf_file(os.path.join(local_paths['conf'], 'connect_alapaca.yml'), False)
print(connection_details)

alpaca_client = TradingClient(connection_details.key, connection_details.secret)
