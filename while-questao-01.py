#Variáveis
soma: int
soma = 0

#Processamento
x = int(input("Digite um número (0 - SAIR): "))
while x != 0:
    soma = soma + x
    x = int(input("Digite um número (0 - SAIR): "))

#Saída
print("Soma vale ", soma)