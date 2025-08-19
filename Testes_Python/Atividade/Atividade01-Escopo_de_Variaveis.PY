variavel_global = "Global"


def minha_funcao():
    
    local_variavel = "Local"
    
    print("Dentro da Função: ")
    print("Variavel Global: ", variavel_global)
    print("Variavel Local: ", local_variavel)
    
minha_funcao()


print("\nFora da Função: ")
print("Variavel global: ", variavel_global)

try:
   print("Variavel Local: ", local_variavel)

except NameError:
    print("Erro: 'Variavel Local' Não está definida fora da função.")