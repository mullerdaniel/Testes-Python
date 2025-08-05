imc = 0
massa = 0.0
altura = 0.0

massa = float(input("Digite o seu peso (KG): "))

altura = float(input("Digite a sua altura: "))
altura = altura ** 2

imc = massa / altura

print("Seu IMC é: ", imc)