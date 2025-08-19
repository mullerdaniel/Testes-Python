
def verificador_media(nota):
    
    if(nota < 7):
        print("Reprovado. Sua media ficou abaixo de 7.")
        
    elif(nota >= 7):
        print("Aprovado. Sua media ficou acima de 7")
        
        
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
media_final = 0.0

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3 = int(input("Digite sua terceira nota: "))
media_final = (nota1 + nota2 + nota3) / 3

verificador_media(media_final)
print("Media Final: ", media_final)