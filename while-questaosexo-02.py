#Declaração de variáveis
qnt = 0
man = 0
woman = 0

#Entrada de dados
nome = input("Digite seu nome: ")
print("Enquanto o sexo digitado for feminino o programa será repetido")
sex = input("Digite seu sexo (M-F): ").upper()
print("="*62)

#Processamento de dados
if sex == "M":
    man = man + 1
else:
    woman = woman + 1

while sex != "M":
    qnt = qnt + 1
    nome = input("Digite seu nome: ")
    print("Enquanto o sexo digittado for masculino o programa será repetido")
    sex = input("Digite seu sexo (M-F): ") .upper()
    print("="*62)
    if sex == "M":
        man = man + 1
    else:
        woman = woman + 1

#Saída de dados
print(f"A quantidade de vezes que o código foi repetido é: {qnt}")
print(f"A quantidade de vezes que o usuário respondeu que seu sexo é musculino foi: {man}")
print(f"A quantidade de vezes que o usuário respondeu que seu sexo é feminino foi: {woman}")