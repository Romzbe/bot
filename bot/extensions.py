import requests
import json
from bot import keys
# from app import value

class APIException(Exception):
    pass



class CriptoConverter:
    @staticmethod
    def convert( q:str, b:str, a:str ):
        try:
            if q == b:
                raise APIException ("Валюты одинаковые")
        except APIException:
            raise APIException ("Валюты одинаковые")

        try:
            qT = keys[q]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {q}")
        try:
            bT = keys[b]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {b}")
        try:
            a = float(a)
        except ValueError:
            raise APIException(f"Неудалось обработать число {a}")
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={qT}&tsyms={bT}')
        tot = json.loads(r.content)[keys[b]]