import pandas as pd

df = pd.read_excel('op-project/exsel/op-team.xlsx',sheet_name='Команда')
def column_data():
    # a = input('Введите имя:')
     column_data = df.iloc[1,1]
     return str(column_data)


