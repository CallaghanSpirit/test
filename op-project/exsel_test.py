import pandas as pd

df = pd.read_excel('op-project/exsel/op-team.xlsx',sheet_name='Команда')
def column_data():
    a = input('Введите имя:')
    ex_data = df[df['Команды']==a] 
    results = [
        int(ex_data['Поступления, руб.'].iloc[0]),
        int(ex_data['Факт поступлений ВСЕГО, руб.'].iloc[0]),
        int(ex_data['Сумма БПВ \nв общих поступлениях, руб.'].iloc[0]),
        int(ex_data['Сумма поступлений по "Правильной ипотеке" или "Траншевой ипотеке"\nв общих поступлениях, руб.'].iloc[0])
    ]
    return results



