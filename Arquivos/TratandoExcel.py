import pandas as pd

listaMeses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in listaMeses:

    print(mes)

    tabelaVendas = pd.read_excel( mes + '.xlsx', engine='openpyxl')

    print(tabelaVendas)



