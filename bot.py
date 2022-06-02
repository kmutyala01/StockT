from os import stat
import alpaca_trade_api as tradeapi

endpoint = 'https://paper-api.alpaca.markets'
api = tradeapi.REST('PKFDOXVK9T7VMFCXG66L','3DjEY2zNTnVqjOd8DaC3hWaJxyF8tYwnrzQ10reW',endpoint)
account = api.get_account()
print(account.status)
