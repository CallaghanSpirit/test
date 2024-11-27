import pandas as pd

df = pd.read_excel('op-project/op-test.xlsx',sheet_name='План-факт')
column_data = df.iloc[6,3]
print(column_data)

