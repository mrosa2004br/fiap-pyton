def opcoes():
    return input("O que deseja reslizar?\n" +
                 "<I> - Inserir um novo usuário\n" +
                 "<P> - Pesquisar um usuário\n" +
                 "<E> - Excluir um usuário\n" +
                 "<L> - Listar usuarios: ").upper()

def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
                                                   input('Digite a última data de acesso: ').upper(),
                                                   input('Qual a última estação acessada: ').upper()]
