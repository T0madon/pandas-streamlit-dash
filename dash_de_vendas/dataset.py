import json
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA = Path(__file__).parent / 'dados/vendas.json'
file = open(DATA)
data = json.load(file)

# print(data)

df = pd.DataFrame.from_dict(data)

# print(df)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()