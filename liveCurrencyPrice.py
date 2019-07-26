import requests
import sys
import colorama

colorama.init()

def crypto_price(name):
    '''
    get live price
    '''
    btc = requests.get(f'https://api.coinmarketcap.com/v1/ticker/{name}').json()
    javab = (f"Price for 1 {name} is {color}{str(btc[0]['price_usd'])}{reset_color}$")
    return javab

color = "\033[94m"
reset_color = "\033[0m"
crp = sys.argv[1]
result = crypto_price(crp)
print(result)
#crypto_list = ['Bitcoin','Ethereum','ripple','Litecoin','Bitcoin-Cash','Binance-Coin','Tether','EOS','Bitcoin-SV','Stellar']


