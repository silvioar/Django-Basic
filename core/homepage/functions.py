from datetime import datetime
import pandas as pd
import numpy as np
import json
import requests


def get_cripto_data():
	tickers = 'bitcoin,chainlink,ethereum,reserve-rights-token,cardano,polkadot,crypto-com-chain'
	url = f'https://api.coingecko.com/api/v3/simple/price?ids={tickers}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true'
	headers = {"accept: application/json"}
	r = requests.get(url = url, verify = False)
	output = r.json()
	df = pd.DataFrame(output).T
	df = df.reset_index()
	df.columns = [['moneda','precio','market_cap','volumen']]
	# Elimino multiindex y los parentesis dentro de los nombres de cada columna
	df.columns = df.columns.get_level_values(0)
	return df