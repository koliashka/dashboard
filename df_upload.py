import os
import pandas as pd

import requests
import pandas as pd
from io import BytesIO


# URL для получения содержимого файла с использованием GitHub API
url = f"https://github.com/koliashka/dashboard/blob/main/data.xlsx"

# Выполнение HTTP-запроса и чтение данных в объект DataFrame с использованием pandas
response = requests.get(url)
df_orders = pd.read_excel(BytesIO(response.content), sheet_name=0)
df_returns = pd.read_excel(BytesIO(response.content), sheet_name=1)



# добавим нформацию о возвратах в заказы
merged_df = pd.merge(df_orders, df_returns[['Order ID', 'Returned']], on='Order ID', how='left')
merged_df['Returned'] = merged_df['Returned'].fillna('No')
