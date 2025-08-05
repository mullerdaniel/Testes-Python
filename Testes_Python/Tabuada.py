contador = 0
soma = 0

numero = int(input("Digite a tabuada que você deseja ver: "))



while contador < 10:
    contador += 1
    soma = numero * contador
   
    print (contador, " X ", numero, " = ", soma)

