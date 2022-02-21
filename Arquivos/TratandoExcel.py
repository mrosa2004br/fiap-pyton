import pandas as pd

listaMeses = ['janeiro','fevereiro','março','abril','maio','junho']
filePath = "excel/"

for mes in listaMeses:

    print(mes)

    tabelaVendas = pd.read_excel( filePath + mes + '.xlsx', engine='openpyxl')

    print(tabelaVendas)



