import math 


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))


delta = b**2 - 4*a*c


if delta < 0:
    print("A equação não possui raízes reais.")
    
    
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    
    print(f"As raízes da equação são: {raiz1} e {raiz2}")
