import requests


# import json

TOKEN = ''

headers = {
  "apikey": ""
}
payload = {}

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    'юань': 'CNY',
    'шекель': 'ILS',
    'рупия': 'INR',
    'вона': 'KRW',
    'бат': 'THB',
    'донг': 'VND',
    'тенге': 'KZT',
    'иена': 'JPY',
    'марка': 'DEM',
    'лира': 'ITL',
    'фунт': 'GBP',
}


texta = 'Для начала работы введите команду боту в формате: \n <название валюты> \n \
<название валюты в которую надо перевести>\n \
<количество переводимой валюты>\n \
Чтобы увидеть список доступных валют, введите: /values\n \
Чтобы увидеть курс доллара к рублю, введите: /dollar\n \
Чтобы увидеть курс евро к рублю, введите: /euro'

txt1 = 'P.s Цены могут незначительно различаться, даже если между запросами прошло несколько секунд, \
из-за постоянного перепада валютного рынка'

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
            raise APIException(f'Не удалось перевести одинаковые валюты - {base}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту - {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту - {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество - {amount}')

        url = f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}"
        response = requests.request("GET", url, headers=headers, data=payload)
        deling = deling_found(response)
        total_base = deling * amount
        total_base = abs(round(total_base, 3))
        return total_base
