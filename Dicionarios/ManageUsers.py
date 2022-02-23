from Dicionarios.Funcoes import *

usuarios = {}
opcao = opcoes()

while opcao=='I' or opcao=='P' or opcao=='E' or opcao=='L':
    if opcao=='I':
        inserir(usuarios)

    opcao = opcoes()

