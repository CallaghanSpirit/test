import pandas as pd

df = pd.read_excel('op-project/op-test.xlsx')
column_data = df['Алан']
print(df.info())
print(column_data.name )
