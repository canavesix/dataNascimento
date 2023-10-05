nome = str(input("Digite seu nome:"))
dataNascimento = int(input("Digite o seu ano de nascimento: "))
dataAtual = 2022




while dataNascimento < 1922 or dataNascimento > 2021:
    print("Digite o seu ano de nascimento:")
    dataNascimento = int(input("Digite um ano de nascimento válido: "))

idadeAtual = dataAtual - dataNascimento

print("Ola", nome , "voce tem" , idadeAtual , "anos !")
