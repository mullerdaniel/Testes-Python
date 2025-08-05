import random

numeroAleatorio = random.randint(0, 100)

numero = int(input(">ADIVINHE O NUMERO<\n\nDigite um numero de 0 a 100: "))

while numero != numeroAleatorio:
    if numero > numeroAleatorio:
        numero = int(input("Digite um número menor: "))
    elif numero < numeroAleatorio:
        numero = int(input("Digite um número maior: "))

print("Parabéns! Você acertou!")