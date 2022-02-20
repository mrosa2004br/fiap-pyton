nome = input("Digite o nome: ")
idade = int( input("Digite a idade: ") )
prioridade = "NÂO"

if idade > 65 :
    prioridade = "SIM"

print("O paciente " + nome + ", " + prioridade + " possui atendimento prioritario. ")
