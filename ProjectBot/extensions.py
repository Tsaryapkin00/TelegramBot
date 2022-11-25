import requests
import json

TOKEN = '5944737183:AAF9Og3lM9_EcotmsFQirAhBFYMkM-Tm_dM'

headers= {
  "apikey": "84279f1113b2539016ac80b78521f49995ee15f742a223314aa451752f8272e7"
}
payload = {}

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}

def deling_found(response):
    deling = response.text.split(':')
    deling = deling.pop()
    deling = deling.split('}')
    deling = deling.pop(0)
    deling = float(''.join(deling))
    return deling

class APIException(Exception):
    pass

class ValuteConvert:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExceptionException(f'Не удалось перевести одинаковые валюты - {base}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIExceptionException(f'Не удалось обработать валюту - {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIExceptionException(f'Не удалось обработать валюту - {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExceptionException(f'Не удалось обработать количество - {amount}')

        url = f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}"
        response = requests.request("GET", url, headers=headers, data=payload)
        deling = deling_found(response)
        total_base = deling * amount
        return total_base