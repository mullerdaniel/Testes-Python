
def verificar_numero(num):
    
    if(num > 0):
        print("O numero é maior que 0")
        
    elif(num < 0):
        print("O numero é menor que 0")
        
    else:
        print("O numero é igual a zero")
        

valor = 0

valor = int(input("Digite um numero: "))
verificar_numero(valor)