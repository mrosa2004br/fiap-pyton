import pandas as pd
import xlrd

listaMeses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in listaMeses:
    print(mes)

tabelaVendas = xlrd.open_workbook("janeiro.xlsx")

##tabelaVendas = pd.read_excel('janeiro.xlsx')

print(tabelaVendas)



