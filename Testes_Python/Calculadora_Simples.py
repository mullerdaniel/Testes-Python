
valor1 = float(input("Digite o primeiro valor: "))

print ("\n\n_______________________________")
print ("|Selecione a operação desejada|")
print ("|1- Adição                    |")
print ("|2- Subtração                 |")
print ("|3- Multiplicação             |")
print ("|4- Divisão                   |")
print ("|_____________________________|")

operacao = int(input("Opção: "))
valor2 = float(input("\nDigite o segundo valor: "))


if operacao == 1:
   print ("\nA soma dos 2 valores é de: ", (valor1 + valor2))
   
if operacao == 2:
    print ("\nA subtração dos 2 valoes é de: ", (valor1 - valor2))     

if operacao == 3:
    print ("\nA multiplicação dos 2 valoes é de: ", (valor1 * valor2))   
    
if operacao == 4:
    print ("\nA divisão dos 2 valoes é de: ", (valor1 / valor2))   